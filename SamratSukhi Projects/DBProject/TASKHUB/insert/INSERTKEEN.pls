create or replace PROCEDURE INSERTKEEN
IS
KID  KEEN.KEENID%TYPE;
	   PASS KEEN.PASSWORD%TYPE;
	   NAME KEEN.NAME%TYPE;
	   G  KEEN.GENDER%TYPE;
     DOB KEEN.DOB%TYPE;
     M  KEEN.MOBILE%TYPE;
     E  KEEN.EMAIL%TYPE;
     A  KEEN.ADDRESS%TYPE;
     J  KEEN.JOIN%TYPE;
     T  KEEN.TASKASK%TYPE;
     DA DATE :=DATE '1997-1-2' ;
     I NUMBER(2);
BEGIN
  A:=CONCAT('A','B');
  FOR I IN 1..25 LOOP
    kid:=concat('K',seq.nextval);
   
    PASS:=CONCAT('PASS',I);
    NAME:=CONCAT('KEEN',I);
    IF MOD(I,2)=0 THEN 
    G:='M';
    ELSE
    G:='F';
    END IF;
    DOB :=  NEXT_DAY(DA,'SUNDAY');
    DA:=DOB;
    M:=7777777777+I;
    E:=CONCAT('EMAIL',CONCAT(I,'@EMAIL.COM'));
    A:=CONCAT('CITY',I);
    J:=SYSDATE;
    T:=0;
  DBMS_OUTPUT.PUT_LINE(KID||PASS||NAME||G||DOB||M||E||A||J||T) ;
  INSERT INTO KEEN (KEENID,PASSWORD,NAME,GENDER,DOB,MOBILE,EMAIL,ADDRESS,JOIN,TASKASK)
  VALUES (KID,PASS,NAME,G,DOB,M,E,A,J,T);
  END LOOP;
END INSERTKEEN;