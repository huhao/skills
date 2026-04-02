#!/usr/bin/env python3
import subprocess
import sys
import os

def check_fonttools():
    try:
        subprocess.check_call(["pyftsubset", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def subset_font(input_path, text_file=None, unicodes=None, output_path=None, flavor="woff2"):
    if not check_fonttools():
        print("错误: 请先安装 fonttools。运行: pip install fonttools brotli")
        sys.exit(1)

    if not os.path.exists(input_path):
        print(f"错误: 找不到输入文件 {input_path}")
        sys.exit(1)

    if not output_path:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}-subset.{flavor}"

    cmd = ["pyftsubset", input_path, f"--flavor={flavor}", f"--output-file={output_path}"]

    if text_file:
        cmd.append(f"--text-file={text_file}")
    elif unicodes:
        cmd.append(f"--unicodes={unicodes}")
    else:
        print("警告: 未指定 text-file 或 unicodes，将精简为空集。")

    print(f"执行命令: {' '.join(cmd)}")
    try:
        subprocess.check_call(cmd)
        print(f"精简完成! 输出文件: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"运行 pyftsubset 失败: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 subset.py <font-path> [--text-file <txt-path>] [--unicodes <range>]")
        sys.exit(1)

    font_path = sys.argv[1]
    text_file_arg = None
    unicodes_arg = None

    if "--text-file" in sys.argv:
        idx = sys.argv.index("--text-file")
        text_file_arg = sys.argv[idx+1]
    
    if "--unicodes" in sys.argv:
        idx = sys.argv.index("--unicodes")
        unicodes_arg = sys.argv[idx+1]

    subset_font(font_path, text_file=text_file_arg, unicodes=unicodes_arg)
