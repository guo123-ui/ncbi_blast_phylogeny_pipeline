#!/bin/bash
# 用途：批量统计一个或多个 FASTA 文件的序列条数和总碱基数
# 使用方法：./fasta_stats.sh tp53.fasta egfr.fasta
#         或 ./fasta_stats.sh *.fasta

# $* 代表脚本接收到的所有参数（所有文件名）
for file in $*; do
    # 打印当前正在处理的文件名，用 === 包围，便于阅读
    echo "=== $file ==="

    # 输出"序列条数："，-n 表示不换行
    echo -n "序列条数: "

    # grep -c 统计匹配的行数
    # "^>" 匹配以 > 开头的行（FASTA 的描述行）
    grep -c "^>" $file

    # 输出"总碱基数："，不换行
    echo -n "总碱基数: "

    # grep -v "^>" 选出不以 > 开头的行（即序列行）
    # tr -d '\n' 删除所有换行符，把多行序列合并成一行
    # wc -c 统计字符数（即总碱基数）
    grep -v "^>" $file | tr -d '\n' | wc -c

    # 打印一个空行，让输出更清晰    
    echo ""
done

