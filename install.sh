#!/bin/bash

mkdir pythonroot
export PYTHONPATH=$PWD/pythonroot/usr/lib/python2.7/site-packages/:$PWD/pythonroot/usr/lib64/python2.7/site-packages/

wget https://files.pythonhosted.org/packages/b7/9d/8209e555ea5eb8209855b6c9e60ea80119dab5eff5564330b35aa5dc4b2c/numpy-1.12.0.zip
unzip numpy-1.12.0.zip
cd numpy-1.12.0
python setup.py install -O2 --root=$PWD/../pythonroot
cd ..
wget https://files.pythonhosted.org/packages/b3/b2/238e2590826bfdd113244a40d9d3eb26918bd798fc187e2360a8367068db/six-1.10.0.tar.gz
tar xf six-1.10.0.tar.gz
cd six-1.10.0
python setup.py install -O2 --root=$PWD/../pythonroot
cd ..
cd matplotlib
python setup.py install -O2 --root=$PWD/../pythonroot
cd ..

rm -rf six-1.10.0 six-1.10.0.tar.gz numpy-1.12.0 numpy-1.12.0.zip
