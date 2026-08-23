Codewriting

Consider an input table `data_name_statistics` that contains four columns:

| Column Name | Type | Description (quotes for clarity) |
| --- | --- | --- |
| `gender` | String | Either `"F"` or `"M"` |
| `decade` | String | One of `"1910s"`, `"1920s"`, `"1930s"`, `"1940s"`, `"1950s"`, `"1960s"`, `"1970s"`, `"1980s"`, `"1990s"`, `"2000s"`, `"2010s"` |
| `name` | String | A non-empty string of a person's given name. |
| `frequency` | Integer (INT64) | The number of newborns of a given name for each gender during each decade. |

For example, the table may look like:

| gender | decade | name | frequency |
| --- | --- | --- | --- |
| F | 1950s | Alice | 35 |
| M | 1960s | John | 27 |
| F | 2010s | Emily | 42 |
| ... | ... | ... | ... |

To help understand the data, you can interact with the following data table to peek at some rows of the table and sort the rows by a chosen column.

Your task is to complete the query, so that the query results will produce a table that contains one row for each decade with the most popular female name (for gender `'F'`) and male name (for gender `'M'`) during the decade in columns `name_f` and `name_m`, respectively. You can assume that the data table contains no ties for the most popular name for each gender and decade pair.

---

**Example**

For given table `name_statistics`:

| gender | decade | name | frequency |
| --- | --- | --- | --- |
| F | 1950s | Alice | 35 |
| M | 1960s | John | 27 |
| F | 2010s | Emily | 42 |
| M | 1960s | Dave | 25 |
| F | 2010s | Sarah | 11 |
| M | 2010s | Evan | 23 |

the output should be:

| decade | name_f | name_m |
| --- | --- | --- |
| 1950s | Alice | NULL |
| 1960s | NULL | John |
| 2010s | Emily | Evan |

* For `1950s`, there is only one name in the given statistics, so it's the most popular: `Alice`. There were no statistics for males in this decade.
* For `1960s`, there are two male's statistics: the name `John` was given to `27` newborns and the name `Dave` to `25`. So `John` was the most popular name in this decade. There were no statistics for females in this decade.
* For `2010s`, there are two female's statistics: the name `Emily` was given to `42` newborns and the name `Sarah` to `11`. So `Emily` was the most popular name in this decade. There were no statistics for males in this decade.

---

**Input/Output**

* **[execution time limit] 10 seconds (mysql)**
* **[memory limit] 1 GB**