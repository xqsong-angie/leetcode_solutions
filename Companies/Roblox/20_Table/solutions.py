import pandas as pd

def get_top_names(df: pd.DataFrame) -> pd.DataFrame:
    # 1. 按 decade 和 gender 分组，并按 frequency 降序排序
    # 2. 每个 (decade, gender) 组合只保留 frequency 最高的一行 (即按顺序去重)
    top_names = df.sort_values(
        by=["decade", "gender", "frequency"], ascending=[True, True, False]
    ).drop_duplicates(subset=["decade", "gender"], keep="first")

    # 3. 使用 pivot 将数据拉平（透视）：
    #    index 为 decade，columns 为 gender，values 为 name
    result = top_names.pivot(
        index="decade", columns="gender", values="name"
    ).reset_index()

    # 4. 重命名列名以符合要求 ('F' -> 'name_f', 'M' -> 'name_m')
    result = result.rename(columns={"F": "name_f", "M": "name_m"})

    # 5. 确保列名顺序正确（如果某个性别在全表中都没出现过，补齐缺失列）
    for col in ["name_f", "name_m"]:
        if col not in result.columns:
            result[col] = None

    # 返回最终结果，按 decade 排序，且列顺序为 decade, name_f, name_m
    return result[["decade", "name_f", "name_m"]].sort_values("decade")