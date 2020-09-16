
# 导入flyai打印日志函数的库
from flyai.utils.log_helper import train_log
# 调用系统打印日志函数，这样在线上可看到训练和校验准确率和损失的实时变化曲线
train_log(train_loss=train_loss, train_acc=train_acc, val_loss=val_loss, val_acc=val_acc)