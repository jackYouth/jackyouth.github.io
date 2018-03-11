#!/usr/bin/env python3
#coding: utf-8
import os

# 真机：db4a4bdf2dab8672f6c9fac853a3cc2fdf404ad2
# 74b75c48e68b1aa821fd0f26405be7f971b6c1cb
# 模拟器： B9B9D3D4-9C6E-4A9C-AF9E-0688724B3660
udid = "db4a4bdf2dab8672f6c9fac853a3cc2fdf404ad2"
api = "/Users/jack/Desktop/fxbank.ipa"
# 测试 /Users/xuguolong/Desktop/installerFlie/fuxinyinhang/pro/PersonalRuntime.ipa
# /Users/xuguolong/Desktop/installerFlie/fuxinyinhang/huidu/BankOfFX_Personal_51734_release_v2.1.0.2.ipa
print("正在安装...")
list(os.popen("""ios-deploy --id {} --bundle {}""".format(udid,api)))
print("安装成功")
