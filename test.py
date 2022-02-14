import sys,sqlite3
def find_employee(kim):
    conn = sqlite3.connect('database.sqlite')
    con = conn.cursor()
    con.execute("SELECT * FROM A_I WHERE kim=?", (str(kim),))
    rows = con.fetchall()

    if len(rows) > 0:
        return rows[0] 
    else:
        return 0
        
#print(list(find_employee("11F589000112582")))


def generate_report():
    data = []
    conn = sqlite3.connect('database.sqlite')
    con = conn.cursor()
    con.execute("SELECT * FROM A_I")
    rows1 = con.fetchall()
    con.execute("SELECT * FROM J_S")
    rows2 = con.fetchall()
    con.execute("SELECT * FROM T_AC")
    rows3 = con.fetchall()
    con.execute("SELECT * FROM AD_AN")
    rows4 = con.fetchall()
    con.execute("SELECT * FROM AM_AW")
    rows5 = con.fetchall()
    con.execute("SELECT * FROM AX_BG")
    rows6 = con.fetchall()
    con.execute("SELECT * FROM BH_BQ")
    rows7 = con.fetchall()
    con.execute("SELECT * FROM BR_CA")
    rows8 = con.fetchall()
    con.execute("SELECT * FROM CB_CW")
    rows9 = con.fetchall()
    con.execute("SELECT * FROM CX_DG")
    rows10 = con.fetchall()
    con.execute("SELECT * FROM DH_DQ")
    rows11 = con.fetchall()
    con.execute("SELECT * FROM DR_EA")
    rows12 = con.fetchall()
    con.execute("SELECT * FROM EB_EK")
    rows13 = con.fetchall()
    con.execute("SELECT * FROM EL_EY")
    rows14 = con.fetchall()
    con.execute("SELECT * FROM EZ_FI")
    rows15 = con.fetchall()
    con.execute("SELECT * FROM FJ_FS")
    rows16 = con.fetchall()
    con.execute("SELECT * FROM FT_GC")
    rows18= con.fetchall()
    con.execute("SELECT * FROM GD_GM")
    rows19 = con.fetchall()
    con.execute("SELECT * FROM GN_GW")
    rows20 = con.fetchall()
    con.execute("SELECT * FROM GX_HK")
    rows21 = con.fetchall()
    print(rows1)
    out = []
    for x in range(0,len(rows2)-1):
        data.extend(list(rows1[x]))
        data.extend(list(rows2[x]))
        data.extend(list(rows3[x]))
        data.extend(list(rows4[x]))
        data.extend(list(rows5[x]))
        data.extend(list(rows6[x]))
        data.extend(list(rows7[x]))
        data.extend(list(rows8[x]))
        data.extend(list(rows9[x]))
        data.extend(list(rows10[x]))
        data.extend(list(rows11[x]))
        data.extend(list(rows12[x]))
        data.extend(list(rows13[x]))
        data.extend(list(rows14[x]))
        data.extend(list(rows15[x]))
        data.extend(list(rows16[x]))
#        data.extend(list(rows17[x]))
        data.extend(list(rows18[x]))
        data.extend(list(rows19[x]))
        data.extend(list(rows20[x]))
        data.extend(list(rows21[x]))
        out.append(data)
    return out

def process(wording, spacing):
    max_len = len(wording)
    if max_len > spacing:
        return wording[0:spacing]
    padding = spacing-max_len
    for i in range(0, padding):
        wording = wording+" "
    return wording
 
def gen(data):
    with open('T.txt','a', encoding = 'utf-8') as f:
        for i in data:
            f.write('\n')
            for j in i:
                f.writelines(process(str(j),12).replace('.',''))

    
print(gen(generate_report()))