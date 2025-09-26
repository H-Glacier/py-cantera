#!/bin/bash

# 定义需要运行的程序的路径
program_path="data_gene_hdf.py"

# 定义不同的参数列表
parameters=($(seq 0 0))

# 循环迭代参数
for param in "${parameters[@]}"; do
    # 构建命令行参数
    command_line="python $program_path $param"

    # 打印当前运行的命令
    echo "Running: $command_line"

    # 执行程序
    $command_line &

    # 可以根据需要添加其他操作，例如日志记录、错误检查等
done

# 等待所有后台进程结束
wait
