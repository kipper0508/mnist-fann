# Test Example of FANN
### FANN
* [DOCS](http://leenissen.dk/fann/wp/)
* [Github](https://github.com/libfann/fann)

### Mnist Dataset
* [THE MNIST DATABASE](http://yann.lecun.com/exdb/mnist/)

### Usage
* Transform idx to txt data
```
usage: python mnist2fann.py [-h] [-L LABEL] [-I IMAGE] [-O OUTPUT]

options:
  -h, --help            show this help message and exit
  -L LABEL, --label LABEL
  -I IMAGE, --image IMAGE
  -O OUTPUT, --output OUTPUT

```
* Compile `C` source code
```
gcc -o train train.c -lfann
```