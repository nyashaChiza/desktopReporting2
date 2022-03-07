def getData():
        conn = sqlite3.connect('database.sqlite')
        con = conn.cursor()
        data = []
        con.execute("SELECT kim FROM AM_AW Where employee_group = ? AND employment_type= ?",[1,100])
        rows5 = con.fetchall()
        girl = 0
        boy=0
        for row in rows5:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where employee_group = ? AND employment_type= ?",[3,210])
        rows4 = con.fetchall()
        girl = 0
        boy=0
        for row in rows4:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where employee_group = ? AND employment_type= ?",[4,100])
        rows3 = con.fetchall()
        girl = 0
        boy=0
        for row in rows3:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where employee_group = ? AND employment_type= ?",[4,210])
        rows1 = con.fetchall()
        girl = 0
        boy=0
        for row in rows1:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where employee_group = ? AND employment_type= ?",[1,100])
        rows6 = con.fetchall()
        girl = 0
        boy=0
        for row in rows6:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where employee_group = ? AND employment_type= ?",[1,210])
        rows7 = con.fetchall()
        girl = 0
        boy=0
        for row in rows7:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where  employment_type= ?",[330])
        rows8 = con.fetchall()
        girl = 0
        boy=0
        for row in rows8:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})

        con.execute("SELECT kim, employee_group,employment_type FROM AM_AW Where  employment_type= ?",[322])
        rows9 = con.fetchall()
        girl = 0
        boy=0
        for row in rows9:
                con.execute(" SELECT gender FROM A_I WHERE kim =?",[row[0]])
                out = con.fetchall()
                if out[0][0] =='2':
                        girl =girl+1
                else:
                        boy =boy+1
        data.append({'boys':boy,'girls':girl})
        return data