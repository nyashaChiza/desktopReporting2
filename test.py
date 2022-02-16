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


def generate_report(start,stop):
    data = []
    conn = sqlite3.connect('database.sqlite')
    con = conn.cursor()
    con.execute("SELECT kim,sin,gender,first_name,last_name,last_name_prefix,academic_title,filler1,birth_date  FROM A_I Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows1 = con.fetchall()
    con.execute("SELECT country_code,postal_code,city,c_o,filler2,filler3,filler4,country_code_mail_address,postal_code_mail_address,city_mail_address FROM J_S Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows2 = con.fetchall()
    con.execute("SELECT date_of_entry_into_group,date_of_leaving_group,reason_for_leaving_the_group, bank_code,bank_account_number,swift_bic,owner_of_bank_account,employee_with_potential,indicator_for_executive,indicator_for_security_advisor FROM T_AC Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows3 = con.fetchall()
    con.execute("SELECT indicator_eligibility_stock_purchase_program,company_code,personal_number,plant_identifier_for_personal_number,filler5,filler6,transfer_date,filler7,filler8,local_cost_center FROM AD_AN Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows4 = con.fetchall()
    con.execute("SELECT employee_group,filler9,department_abbreviation,hr_executive_level,employment_type,organizational_code,physical_work_location_code,internal_mail_code,level_of_business_allocation1,level_of_business_allocation2 FROM AM_AW Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows5 = con.fetchall()
    con.execute("SELECT mailing_language_of_employee,building,room_number,location_code,country_of_birth,city_of_birth,citizenship,filler10,filler11,street_and_house_number_of_home_address FROM AX_BG Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows6 = con.fetchall()
    con.execute("SELECT street_and_house_number_for_preferred_mailing_address,filler12,job_code,plant2,plant1,organizational_code2,smtp_email_address,position_entry_date,date_contract_end,hr_department FROM BH_BQ Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows7 = con.fetchall()
    con.execute("SELECT hr_representative,fax_number_hr_representative,management_level,work_phone_number_of_hr_representative,preferred_first_name,middle_initial,home_host_indicator,fulltime_parttime_equivalency,reports_to_kim,date_of_entry_into_company FROM BR_CA Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows8 = con.fetchall()
    con.execute("SELECT filler12,filler13,filler14,filler15,filler16,filler17,filler18,filler19,filler20,filler21,filler22,filler23,filler24,filler25,filler26,filler27,filler28,filler29,filler30,filler31,filler32,filler33 FROM CB_CW Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows9 = con.fetchall()
    con.execute("SELECT current_position_title,payment_type,plant_section,filler35,indicator_for_disabled_person,social_security_number,state,state_for_preferred_mailing_address,phone_country_code FROM CX_DG Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows10 = con.fetchall()
    con.execute("SELECT phone_country_code,phone_extension_and_company,fax_country_code,fax_area_code,fax_extension_and_company,mobile_country_code,mobile_area_code,mobile_number,empl_id,filler36 FROM DH_DQ Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows11 = con.fetchall()
    con.execute("SELECT filler37,bv_wechsel_ab,wohnhaft_bei,company_code_expat,currency,filler38,year_of_goal_income,monthly_salary,delete_flag,filler39 FROM DR_EA Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows12 = con.fetchall()
    con.execute("SELECT grade_band,shift_indicator,employee_category,department_name,status_employee,code_dl_tv,grade,nacos_cost_center,wage_group,year_of_wage_group FROM EB_EK Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows13 = con.fetchall()
    con.execute("SELECT date_of_assignment_to_wage_group,filler40,logon_id_of_employee,company_name_of_external_person,filler41,filler42,filler43,filler44,filler45,filler46,filler47,filler48,filler49,filler50 FROM EL_EY Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows14 = con.fetchall()
    con.execute("SELECT bv_wechsel_ab,filler51,filler52,type_of_timeframe_for_tax_data,starting_of_timeframe_for_tax_data,end_of_timeframe_for_tax_data FROM EZ_FI Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows15 = con.fetchall()
    con.execute("SELECT starting_of_timeframe_for_tax_data,end_of_timeframe_for_tax_data,type_of_timeframe_for_tax_data FROM FJ_FS Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows16 = con.fetchall()
    con.execute("SELECT end_of_timeframe_for_tax_data,type_of_timeframe_for_tax_data,starting_of_timeframe_for_tax_data FROM FT_GC Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows18= con.fetchall()
    con.execute("SELECT type_of_timeframe_for_tax_data,starting_of_timeframe_for_tax_data,end_of_timeframe_for_tax_data FROM GD_GM Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows19 = con.fetchall()
    con.execute("SELECT permanent_residence,filler54,wage_and_salary_group,diversity,executive_bonus,number_of_monthly_base_salary,structure_code,dept_id,full_time_equivalent,bonus_payout FROM GN_GW Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows20 = con.fetchall()
    con.execute("SELECT position_control_number,daimler_cost_center,last_name_passport,first_name_passport,executive_bonus,iban,local_job_profile,irwwh,buchungskreis,rabattkennzeichen,valid_by,widersprecherkennzeichen,ivv_contract,ivv_risk_taker,ivv_control_unit FROM GX_HK Where date_entry BETWEEN date(?) and date(?)",[start,stop])
    rows21 = con.fetchall()
    print('rows:',len(rows1))
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
        data = []
    return out

def process(wording, spacing):
    max_len = len(wording)
    
    padding = abs(spacing-max_len)
    for i in range(0, padding):
        wording = wording+" "
    return wording
 
def gen(data):

    with open('T.txt','w', encoding = 'utf-8') as f:
        for i in data:
            f.write('\n')
            count =0
            for j in i:
                count = count + 1
                if count == 66 and j[0] != ' ':
                   # print(len(j))
                    f.writelines((process(j[:45]+' '.lstrip(),12).replace('.','')).replace('-',''))
                else:
                    f.writelines((process(str(j),12).replace('.','')).replace('-',''))
print(gen(generate_report('2000-10-10','2022-02-19')))
#---------------------------------------------------------------------------------------------------------------------
def dateCheck(arg,value):
            result = []
            maps=[]
            if len(value[0])==1:
                maps.append(1)
            else:
                maps.append(0)
            if len(value[1])== 1:
                maps.append(1)
            else:
                maps.append(0)
           
            if arg == 'to':
                if maps[0] ==1:
                       result.append('0')
                else:
                        result.append('')
                if maps[1] ==1:
                       result.append('-0')
                else:
                        result.append('-')
                return result[0]+value[2]+result[1]+value[0]+'-'+value[1]
            else:
                if maps[0] ==1:
                       result.append('0')
                else:
                        result.append('')
                if maps[1] ==1:
                       result.append('-0')
                else:
                        result.append('-')
               
                return result[0]+value[2]+result[1]+value[0]+'-'+value[1]
                        
#---------------------------------------------------------------------------------------------------------------------
#print(dateCheck('ffrom',['1','2','2022']))