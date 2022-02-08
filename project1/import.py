
import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine= create_engine(postgresql://dmrvmtjnwpyzug:5fa2fcea15f8b078d83e43c4b47a71614adf0058ad4fa96e698f1185d972f654@ec2-54-157-15-228.compute-1.amazonaws.com:5432/dcskcrfmq395or')

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

lef main():
 f=open("books.csv")
 reader = csv.reader(f)
 for isbn, title, author, year in reader:
     db.excute("INSERT INTO  books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
     {"isbn":isbn, "title": title, "author": author, "year": year})
     db.commit()

     __name__=="__main__"
     main()




















#
