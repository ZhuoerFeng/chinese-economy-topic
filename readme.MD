# 中国经济专题 期末作业
第21组

## 文件说明
`did_data.csv`：DiD差分原始数据
`did_input.csv`：DiD差分模型输入数据
`east.csv`：东部地区省数据
`middle.csv`：东部地区省数据
`west.csv`：东部地区省数据
`pro.py`：数据处理、DiD回归代码
`control_variables/`：控制变量数据目录
`core_variables/`：核心变量数据目录
`数据实验.xlsx`：实验结果记录表

## 运行方式

在`did_input.csv`同级的目录下，使用终端运行
``` python3 run.py```
观察输出logging的打印

在`run.py`的`main()`第343行分别修改为`df = pd.read_csv('east.csv')`，`df = pd.read_csv('middle.csv')`，`df = pd.read_csv('west.csv')`即可运行东部、中部、西部城市数据的模型拟合情况
