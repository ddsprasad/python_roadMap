def delete_tbl(dbhost, dbuser, dbpass, dbschema, tblName, issuerId):
    
    import mysql.connector

    mydb = mysql.connector.connect(
        host=dbhost,
        user=dbuser,
        password=dbpass,
        database=dbschema,
        ssl_verify_cert=True,
        ssl_ca=certfilePath
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM %s WHERE issuer_id = %s" % (tblName, issuerId)

    print(sql)

    mycursor.execute(sql)

    mydb.commit()