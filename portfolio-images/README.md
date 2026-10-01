# Project image gallery

Twelve PNG images, each **1920 × 1080**, with consistent frames, margins, and alignment. The main [repository README](../README.md#project-showcase) selects the result examples and implementation views most useful for reviewing the project.

## Capture index

| Image | Type | Content |
| --- | --- | --- |
| [01 · Execution startup](01-execution-startup.png) | Recorded startup | Actual CrewAI, task, and analyst startup messages for BMW. |
| [02 · Crew orchestration](02-crew-orchestration.png) | Source capture | `crew.py` and the local snapshot's `main.py`. |
| [03 · Financial Market Analyst](03-financial-market-analyst.png) | Source capture | Analyst role, LLM configuration, and tool access. |
| [04 · Strategic Stock Trader](04-strategic-stock-trader.png) | Source capture | Trader role and LLM configuration. |
| [05 · Stock-information tool](05-live-stock-information-tool.png) | Source capture | The actual Yahoo Finance lookup and price/change formatter. |
| [06 · Analysis and trading tasks](06-analysis-and-trading-tasks.png) | Source capture | Task definitions from the local CLI snapshot. |
| [07 · Demo crew startup](07-demo-crew-startup.png) | Synthetic demo | Scripted crew, task, and analyst startup. |
| [08 · Demo tool result](08-demo-stock-tool-result.png) | Synthetic demo | The original research function evaluated against a local fixture. |
| [09 · Demo market analysis](09-demo-market-analysis.png) | Synthetic demo | Scripted analyst response for that fixture. |
| [10 · Demo trader startup](10-demo-trader-startup.png) | Synthetic demo | Scripted trading-task and trader startup. |
| [11 · Demo recommendation](11-demo-trading-decision.png) | Synthetic demo | Scripted HOLD response and task completion. |
| [12 · Demo final result](12-demo-final-result.png) | Synthetic demo | Scripted final crew output. |

## Provenance

The captures were prepared from a local CLI snapshot. The published repository also includes `streamlit_app.py` and risk-tolerance / investment-horizon inputs, which are not shown in these images. Source captures 02 and 06 predate those profile inputs; the main README uses the unchanged analyst and research-tool captures instead. These images are console and source views, not screenshots of the Streamlit interface.

The real local run started under Python 3.11.15 with CrewAI 1.8.1, but Groq returned `model_not_found` for the configured model. Image 01 shows startup only; it does not establish that either agent completed a task.

Images **07–12** are user-requested dummy results. Every image displays **DEMO · SYNTHETIC RESULTS** and states that there were no live API or LLM calls. CrewAI's existing console formatter rendered the panels. Agent responses and completion events were scripted.

The synthetic BMW fixture uses a price of **188.4 EUR** and a change of **-1.6 EUR (-0.84%)**. The original `get_stock_price` function body was evaluated against that fixture; its output format was preserved. Volume, volatility, and historical momentum remain explicitly unavailable. The data and responses are stored in [demo-results.json](demo-results.json).

[manifest.json](manifest.json) records capture types and hashes of the source snapshot. References to local capture transcripts, dependency files, and the capture runtime are provenance records; that tooling is not distributed with the repository. No application source was changed to create these images, and credentials are excluded.
