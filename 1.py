#!/usr/bin/python
# -*- coding: UTF-8 -*-
#建立一个sshclient对象
import paramiko
import sys
ssh = paramiko.SSHClient()
# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname='10.20.57.254', port=22, username='admin', password='huawei123')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('show wir radio')
# 结果放到stdout中，如果有错误将放到stderr中
print(stdout.read().decode())
# 关闭连接
ssh.close()

####
