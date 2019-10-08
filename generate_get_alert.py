dados_json = [11.211200,"index0.ts",9.609600,"index1.ts",9.609600,"index2.ts",9.609600,"index3.ts",11.211200,"index4.ts",9.609600,"index5.ts",9.609600,"index6.ts",9.609600,"index7.ts",11.211200,"index8.ts",9.609600,"index9.ts",9.609600,"index10.ts",9.609600,"index11.ts",11.211200,"index12.ts",9.609600,"index13.ts",9.609600,"index14.ts",9.609600,"index15.ts",11.211200,"index16.ts",9.609600,"index17.ts",9.609600,"index18.ts",9.609600,"index19.ts",11.211200,"index20.ts",9.609600,"index21.ts",9.609600,"index22.ts",9.609600,"index23.ts",11.211200,"index24.ts",9.609600,"index25.ts",9.609600,"index26.ts",9.609600,"index27.ts",11.211200,"index28.ts",9.609600,"index29.ts",9.609600,"index30.ts",9.609600,"index31.ts",11.211200,"index32.ts",9.609600,"index33.ts",9.609600,"index34.ts",9.609600,"index35.ts",11.211200,"index36.ts",9.609600,"index37.ts",9.609600,"index38.ts",9.609600,"index39.ts",9.609600,"index40.ts",11.211200,"index41.ts",9.609600,"index42.ts",9.609600,"index43.ts",9.609600,"index44.ts",11.211200,"index45.ts",9.609600,"index46.ts",9.609600,"index47.ts",9.609600,"index48.ts",1.201200,"index49.ts"]

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
            "uuid_fragmento": "05b6db49-4f61-477c-8f21-6a0d40794324"
        }
"""

start = 0
for x in range(0, len(dados_json), 2):
    if(x != 0 ):
        start += dados_json[x]

    print(json.replace("{replace_seq_start}", str(start)).replace("{replace_name}",dados_json[x+1]))
    print(',')