dados_json = [11.520000, "index0.ts", 9.600000, "index1.ts", 9.600000, "index2.ts", 9.600000, "index3.ts", 11.520000, "index4.ts", 9.600000, "index5.ts", 9.600000, "index6.ts", 9.600000, "index7.ts", 9.600000, "index8.ts", 11.520000, "index9.ts", 9.600000, "index10.ts", 9.600000, "index11.ts", 9.600000, "index12.ts", 9.600000, "index13.ts", 11.520000, "index14.ts", 9.600000, "index15.ts", 9.600000, "index16.ts", 9.600000, "index17.ts", 9.600000, "index18.ts", 11.520000, "index19.ts", 9.600000, "index20.ts", 9.600000, "index21.ts", 9.600000, "index22.ts", 9.600000, "index23.ts", 1.160000, "index24.ts"]
json = """
{
            "alerts": {
                "moviment": false,
                "other": false,
                "person": false,
                "thumbnail": ""
            },
            "seg_start": {replace_seq_start},
            "name": "{replace_name}",
        }
"""

start = 0
for x in range(0, len(dados_json), 2):
    if(x != 0 ):
        start += dados_json[x]

    print(json.replace("{replace_seq_start}", str(start)).replace("{replace_name}",dados_json[x+1]))
    print(',')
