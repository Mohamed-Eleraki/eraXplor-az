![https://github.com/Mohamed-Eleraki/eraXplor/blob/master/docs/assets/images/eraXplor.jpeg](https://github.com/Mohamed-Eleraki/eraXplor/blob/master/docs/assets/images/eraXplor.jpeg)

Azure Cost Export Tool for automated cost reporting and analysis.

**eraXplor** is an automated Azure cost reporting tool designed for assest DevOps and FinOps teams fetching and sorting Azure Cost Explorer.
it extracts detailed cost data by using Azure SDKs Libraries and Transform result into a CSV.
`eraXplor` gives you the ability to sort the cost by subscriptions, as well as format and separate the result by Monthly or Daily cost.

## Key Features

- ✅ **subscription-Level Cost Breakdown**
- ✅ **Daily/Monthly Cost Breakdown**
- ✅ **Flexible Date Ranges**: Custom start/end dates with validation.
- ✅ **Support secure authentication**: By fetching Azure credentials configured within terminal.
- ✅ **CSV Export**: Ready-to-analyze reports in CSV format.
- ✅ **Cross-platform CLI Interface**: Simple terminal-based workflow, and **Cross OS** platform.
- ✅ **Documentation Ready**: Well explained documentations assest you kick start rapidly.
- ✅ **Open-Source**: the tool is open-source under Apache 2.0 license, which enables your to enhance it for your purpose.

---

## Table Of Contents

Quickly find what you're looking for:

1. [Welcome to eraXplor](https://mohamed-eleraki.github.io/eraXplor/)
2. [Tutorials](https://mohamed-eleraki.github.io/eraXplor/tutorials/)
3. [How-To Guides](https://mohamed-eleraki.github.io/eraXplor/how-to-guides/)
4. [Explanation](https://mohamed-eleraki.github.io/eraXplor/explanation/)
5. [Reference](https://mohamed-eleraki.github.io/eraXplor/reference/)

---

## Why eraXplor?

![https://github.com/Mohamed-Eleraki/eraXplor/blob/master/docs/assets/images/why_eraXplor.jpeg](https://github.com/Mohamed-Eleraki/eraXplor/blob/master/docs/assets/images/why_eraXplor.jpeg)

# How-To Guides

## Azure Profile Configuration

- Install [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest&pivots=apt) - Command line tool.
- authenticate with azure portal by:

```bash
az login
```

## Check installed Python version

- Ensure you Python version is >= 3.12.3 by:

```bash
python --version

# Consider update Python version if less than 3
```

## Install eraXplor

- Install eraxplor tool by:

```bash
pip install eraXplor_az
```

## How-To use

`eraXplor` have multiple arguments set with a default values _-explained below-_, Adjsut these arguments as required.

```bash
usage: eraXplor_az [-h] [-s START_DATE] [-e END_DATE] -S SUBSCRIPTION_ID [-g {Daily,Monthly}] [-o OUT]

Export Azure cost data for using Azure Cost Management API.

options:
  -h, --help            show this help message and exit
  -s START_DATE, --start-date START_DATE
                        Start date for cost export in YYYY,MM,DD format. (default: 2025,04,21)
  -e END_DATE, --end-date END_DATE
                        End date for cost export in YYYY,MM,DD format. (default: 2025,07,20)
  -S SUBSCRIPTION_ID, --subscription-id SUBSCRIPTION_ID
                        Azure subscription ID for cost export. (default: None)
  -g {Daily,Monthly}, --granularity {Daily,Monthly}
                        Granularity of cost data (Daily or Monthly). Default is Monthly. (default: Monthly)
  -o OUT, --out OUT     CSV output filename. (default: az_cost_report.csv)
```

For Windows/PowerShell users restart your terminal, and you may need to use the following command:

```bash
python3 -m eraXplor_az

# Or
python -m eraXplor_az

# to avoid using this command, apend the eraXplor to your paths.
# Normaly its under: C:\Users\<YourUser>\AppData\Local\Programs\Python\Python<version>\Scripts\
```

<details open>
<summary><strong> ℹ️ Notes </strong></summary>

    Ensure you run the command in a place you have sufficient permission to replace file.
    *The eraXport tool sorting cost reult into a CSV file, by default The CSV will replace for next run.*
</details>

### Argument Reference

-h, --help            show this help message and exit
-s START_DATE, --start-date START_DATE
                      Start date for cost export in YYYY,MM,DD format. (default: 2025,04,21)
-e END_DATE, --end-date END_DATE
                      End date for cost export in YYYY,MM,DD format. (default: 2025,07,20)
-S SUBSCRIPTION_ID, --subscription-id SUBSCRIPTION_ID
                      Azure subscription ID for cost export. (default: None)
-g {Daily,Monthly}, --granularity {Daily,Monthly}
                      Granularity of cost data (Daily or Monthly). Default is Monthly. (default:Monthly)
-o OUT, --out OUT     CSV output filename. (default: az_cost_report.csv)

<!-- ```mermaid
graph LR
    A[Azure Console] ->|Complex UI| B[Manual Export]
    B -> C[Spreadsheet Manipulation]
    D[eraXplor] ->|Automated| E[Standardized Reports]
    style D fill:#4CAF50,stroke:#388E3C
    Replace -> with double --
``` -->
<br><br>
<details open>
<summary><strong>👋Show/Hide Author Details👋</strong></summary>

**Mohamed eraki**  
_Cloud & DevOps Engineer_

[![Email](https://img.shields.io/badge/Contact-mohamed--ibrahim2021@outlook.com-blue?style=flat&logo=mail.ru)](mailto:mohamed-ibrahim2021@outlook.com)  
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-informational?style=flat&logo=linkedin)](https://www.linkedin.com/in/mohamed-el-eraki-8bb5111aa/)  
[![Twitter](https://img.shields.io/badge/Twitter-Follow-blue?style=flat&logo=twitter)](https://x.com/__eraki__)  
[![Blog](https://img.shields.io/badge/Blog-Visit-brightgreen?style=flat&logo=rss)](https://eraki.hashnode.dev/)

### Project Philosophy

> "I built eraXplor to solve real-world cloud cost visibility challenges — the same pain points I encounter daily in enterprise environments. This tool embodies my belief that financial accountability should be accessible to every technical team."

</details>
