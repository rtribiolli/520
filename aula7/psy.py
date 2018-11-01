from psycopg2 import connect

try:
    con = connect('host = localhost dbname=projeto user=admin password=4linux')
    cur = con.cursor()

except Exception as e:
    print('ERRO: {}'.format(e))
    exit()

#cur.execute("select * from produtos where preco between '5' and '100';")
#print(cur.fetchall())
cur.execute("insert into produtos (nome, preco, quantidade) values('livro', '200', '50');")
con.commit()

cur.close()
con.close()
