# 导入工具库：正则用于查找密码子，matplotlib用于绘制饼图
import re
import matplotlib.pyplot as plt

# 1. 打开原始FASTA文件（只读模式，不修改原文件）
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
# 初始化密码子计数字典：key为密码子，value为出现次数
codon_counts = {}

stop_codon = input("Please input one of the three codons(TAA/TAG/TGA):")

current_gene = ""
current_seq = ""

# 4. 逐行读取文件，处理每个基因
for line in input_file:
    # 去除行尾换行符和多余空格
    line = line.rstrip()

    # 区分标题行（以>开头）和序列行
    if line.startswith('>'):
        # 若已有上一个基因，先处理上一个基因
        if current_gene != "":
            # 4.1 找到当前基因中所有指定终止密码子的起始位置
            stop_positions = [m.start() for m in re.finditer(stop_codon, current_seq)]
            # 4.2 找到基因的起始密码子ATG的位置（取第一个ATG作为ORF起点）
            atg_match = re.search(r'ATG', current_seq)
            # 4.3 仅处理同时有ATG和终止密码子的有效ORF
            if atg_match and len(stop_positions) > 0:
                atg_pos = atg_match.start()
                # 4.4 筛选ATG之后的终止密码子，取最远的一个（保证最长ORF）
                valid_stops = [pos for pos in stop_positions if pos > atg_pos]
                if len(valid_stops) > 0:
                    longest_stop_pos = max(valid_stops)
                    # 4.5 提取ORF序列：从ATG到终止密码子前
                    orf_seq = current_seq[atg_pos : longest_stop_pos]
                    # 4.6 提取框内密码子：每3个碱基为一个，保证相位正确
                    for i in range(0, len(orf_seq), 3):
                        # 过滤不完整的3碱基片段
                        if i + 3 <= len(orf_seq):
                            codon = orf_seq[i:i+3]
                            # 更新密码子计数
                            if codon in codon_counts:
                                codon_counts[codon] = codon_counts[codon] + 1
                            else:
                                codon_counts[codon] = 1

            # 4.7 更新为当前新基因的信息
            current_gene = line[1:].split(' ')[0]
            current_seq = ""
        else:
            # 第一个标题行，直接赋值基因名
            current_gene = line[1:].split(' ')[0]
            current_seq = ""
    else:
        # 序列行：合并到当前基因的完整序列中
        current_seq = current_seq + line

# 5. 处理最后一个基因（文件末尾无新标题行，单独处理避免遗漏）
if current_gene != "":
    stop_positions = [m.start() for m in re.finditer(stop_codon, current_seq)]
    atg_match = re.search(r'ATG', current_seq)
    if atg_match and len(stop_positions) > 0:
        atg_pos = atg_match.start()
        valid_stops = [pos for pos in stop_positions if pos > atg_pos]
        if len(valid_stops) > 0:
            longest_stop_pos = max(valid_stops)
            orf_seq = current_seq[atg_pos : longest_stop_pos]
            for i in range(0, len(orf_seq), 3):
                if i + 3 <= len(orf_seq):
                    codon = orf_seq[i:i+3]
                    if codon in codon_counts:
                        codon_counts[codon] = codon_counts[codon] + 1
                    else:
                        codon_counts[codon] = 1

# 6. 关闭输入文件，释放资源
input_file.close()

# 7. 生成符合要求的饼图
# 7.1 提取密码子和对应计数
codons = list(codon_counts.keys())
counts = list(codon_counts.values())

# 7.2 设置饼图画布和标题（纯+拼接，无f-string）
plt.figure(figsize=(12, 12))
title = "Codon Frequency for Stop Codon: " + stop_codon + "\nTotal Codons Counted: " + str(sum(counts))
plt.title(title, fontsize=16)

# 7.3 绘制饼图，标注百分比，调整样式
wedges, texts, autotexts = plt.pie(
    counts, 
    labels=codons, 
    autopct='%1.1f%%', 
    startangle=90
)
# 调整标签字体大小和颜色，提升可读性
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_color('white')

# 7.4 保存饼图到文件（任务要求：必须保存，而非仅显示）
plt.savefig('codon_frequency_' + stop_codon + '.png', bbox_inches='tight')
# 7.5 在屏幕上显示饼图
plt.show()

# 8. 打印排序后的统计结果，方便用户核对
for codon, count in sorted(codon_counts.items(), key=lambda x: x[1], reverse=True):
    print(codon + ": " + str(count) + " times")