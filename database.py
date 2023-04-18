
from sqlalchemy import create_engine,text

db_connection_string ="mysql+pymysql://x8bmcd2f4mv6frfbhc8n:pscale_pw_2tJSy2FQtfDdQWcafaaOx4eKxNPJaM6wZofBH8uJe5P@aws.connect.psdb.cloud/joviancarrerf?charset=utf8mb4"


engine = create_engine(db_connection_string,
      connect_args= {
         "ssl" :{
            "ssl_ca": "/etc/ssl/cert.pem"
         }
      })

def load_jobs_from_db():
 with engine.connect() as conn:
     result = conn.execute(text("select * from jobs"))
     result_all = result.all()
     print(result_all)
     print("type(result):",type(result))
     first_result = result_all[0]
     print("type(first_result):",type(first_result))
     first_result_dict = dict(result_all[0])
     print("type(first_result_dict):",type(first_result_dict))
     print(first_result_dict)

  

   