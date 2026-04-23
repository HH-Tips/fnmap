#!/bin/bash
git clone https://github.com/HH-Tips/fnmap.git ~/.local/share/fnmap
ln -s ~/.local/share/fnmap/fnmap .local/bin/fnmap

echo "If 'which fnmap' returns no fnmap found add .local/bin/ to your \$PATH env variable."