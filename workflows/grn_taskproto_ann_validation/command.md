## Command

命令名称：

```text
/grn_taskproto_ann_validation
```

标准调用格式：

```text
/grn_taskproto_ann_validation <input_file> --mode balanced --top_k 3
```

示例：

```text
/grn_taskproto_ann_validation eq.md --top_k 3
```

可选参数：

- --mode: conservative | balanced | aggressive
- --top_k: 输出的任务原型数量

默认行为：

- 使用固定任务原型库默认版本
- 使用默认 ANN 家族列表

停顿等待人类确认的步骤：

- Stage C 完成后触发 checkpoint_c1
