#!/bin/bash
# need to configure the root directory manually
# the command in TexStudio may look like this
# bash /home/alan/LocalDocument/PRML_Project/script/tex_studio_compile.sh ?m) | txs:///view-pdf-internal /home/alan/LocalDocument/PRML_Project/temp/prml_ans_?m).pdf

cd ~/LocalDocument/PRML_Project
python3 ./inspect_answer.py -s $1 -n