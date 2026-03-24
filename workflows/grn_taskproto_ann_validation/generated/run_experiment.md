# Run Experiment

experiment_input:
  file: workflows/grn_taskproto_ann_validation/test_run/input_grn_krumsiek11_like.json
  grn_items: ["grn_krumsiek11_like"]
  prototype_library_ref: "data/prototypes/v1"

run_command:
  "python workflows/grn_taskproto_ann_validation/test_run/run_workflow_smoke.py"

execution_trace_summary:
  - Stage A: task_prototype_library_builder、probe_compiler、pirg_builder 执行成功
  - Stage B: grn_intake、grn_observer、pirg_builder 执行成功，GRN 输入为 krumsiek11_like
  - Stage C: distance_engine、pot_gw_adapter、ott_jax_gw_adapter 执行成功并产出 Top-K
  - checkpoint_c1: 已触发并记录
  - Stage D: ann_runner、ann_observer、mamba_ssm_adapter 执行成功
  - Stage E: validator、result_reporter 执行成功并生成 validation_report.md
  - 外部候选仓库：POT/ott-jax/pySCENIC/mamba 已下载，scanpy 受 Windows 路径长度影响为部分 checkout
  - ClawHub 技能检索与安装：gene2ai-openclaw-skill、flow-cytometry-gating-strategist 已落盘
  - 外部技能联调：flow-cytometry-gating-strategist 可运行并生成建议结果，gene2ai 因缺少 API key 跳过

checkpoint_events:
  - checkpoint_c1 triggered after stage_c

outputs_generated:
  - workflows/grn_taskproto_ann_validation/test_run/artifacts/topk_task_prototypes.json
  - workflows/grn_taskproto_ann_validation/test_run/artifacts/ranked_ann_results.json
  - workflows/grn_taskproto_ann_validation/test_run/artifacts/validation_report.md
  - workflows/grn_taskproto_ann_validation/test_run/artifacts/workflow_smoke_summary.json
  - workflows/grn_taskproto_ann_validation/test_run/artifacts/flow_cytometry_recommendation.json

pass_fail_judgement: partial

issues_and_fixes:
  - 当前 GRN 为可用的 krumsiek11_like 示例网络，非真实实验数据
  - POT/OTT/pySCENIC/mamba 为代码快照下载状态，未完成环境安装，适配层自动走 fallback
  - scanpy 仓库在 Windows 下部分测试资源路径过长，主代码已下载可引用
  - flow-cytometry-gating-strategist 安装时触发 VirusTotal suspicious 警告，已执行最小调用但建议人工审计后再进入自动主路径
  - gene2ai-openclaw-skill 需要 GENE2AI_API_KEY 才能执行真实查询

---

realgw_run:
  experiment_input:
    file: workflows/grn_taskproto_ann_validation/external_candidates/scanpy/tests/_data/10x_data/1.2.0/filtered_gene_bc_matrices/hg19_chr21/matrix.mtx
    genes_used:
      - RUNX1
      - ETS2
      - ERG
      - IFNAR1
      - IFNAR2
      - IL10RB
      - RCAN1
      - SOD1
      - CBS
      - BACH1
  run_command:
    - python -m pip install POT
    - python workflows/grn_taskproto_ann_validation/test_run/run_workflow_realgw.py
  outputs_generated:
    - workflows/grn_taskproto_ann_validation/test_run/realgw_artifacts/topk_task_prototypes_realgw.json
    - workflows/grn_taskproto_ann_validation/test_run/realgw_artifacts/ranked_ann_results_realgw.json
    - workflows/grn_taskproto_ann_validation/test_run/realgw_artifacts/validation_report_realgw.md
    - workflows/grn_taskproto_ann_validation/test_run/realgw_artifacts/workflow_realgw_summary.json
  key_results:
    - top_prototype: Proto-Switch (GW=0.6680)
    - ann_best_by_gw: sparse_mlp (GW=0.9592)
    - rank_consistency_spearman: -0.800
    - judgement: preliminary_inconclusive
  pass_fail_judgement: partial
