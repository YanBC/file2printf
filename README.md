# Description
This script perform a basic simple task: transform a text file to C/C++ string. I don't know what's your user case. For me, I find myself often in a situation where I am writing a bash script and have to create a predefined configuration file. I normally just ```printf``` it as below. This script can come in handy.
```bash 
printf <c/c++ style string>
```

# Usage
```bash
python3 transform <src_file>
```

# Demo
```bash
git clone https://github.com/YanBC/file2printf.git
cd file2printf
python3 transform.py test_config.json 
```

Output:
```
"{\n    \"server\":\"baidu.com\",\n    \"server_port\":3321,\n    \"local_address\":\"127.0.0.1\",\n    \"local_port\":1080,\n    \"password\":\"dsadf\",\n    \"method\":\"chacha20-ietf-poly1305\"\n}\n"
```