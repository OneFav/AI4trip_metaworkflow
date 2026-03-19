# consistency_checker

## Role

检查仿真结果与数学求解结论的一致性与偏差来源。

## Input

* simulation_summary
* solver_results
* assumption_registry

## Output

* consistency_report
* discrepancy_items

## Constraints

每条偏差必须绑定到具体参数段或假设项。
