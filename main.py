
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 22:17:56 2022

@author: Flia. Rodriguez
"""
from iqoptionapi.stable_api import IQ_Option
import time
import threading
from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
modo_cuenta = "REAL"
stop_hilo5 = "run" 
profit5 = 0.10
#############################################################################################  
      
    
def antesala_panel1_stop(_stop_h1):
    global stop_hilo1
    stop_hilo1 = _stop_h1

def antesala_panel2_stop(_stop_h2):
    global stop_hilo2
    stop_hilo2 = _stop_h2

def antesala_panel3_stop(_stop_h3):
    global stop_hilo3
    stop_hilo3 = _stop_h3
    
def antesala_panel4_stop(_stop_h4):
    global stop_hilo4
    stop_hilo4 = _stop_h4
    
def antesala_panel5_stop(_stop_h5):
    global stop_hilo5
    stop_hilo5 = _stop_h5   
    
def antesala_panel1(estrategia, money, par, modo_entrada, mg_modo, martin_gale, stop_gain, stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):
   
    _estrategia = str(estrategia)
    _money = int(money)
    _par = str(par)
    _modo_entrada = int(modo_entrada)
    _mg_modo = int(mg_modo)
    _mg = int(martin_gale)
    _stop_gain = int(stop_gain)
    _stop_loss = int(stop_loss)
    _hora_limite = int(hora_limite)
    _minuto_limite = int(minuto_limite)  
    
    if _estrategia == "MHI":    
     hilo1 = threading.Thread(target=mhi, args=(_money, _par, _modo_entrada, _mg_modo, _mg, _stop_gain, _stop_loss, _hora_limite, _minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest))  
     hilo1.start()
     
def antesala_panel2(estrategia, money, par, modo_entrada, mg_modo, martin_gale, stop_gain, stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):

    _estrategia = str(estrategia)
    _money = int(money)
    _par = str(par)
    _modo_entrada = int(modo_entrada)
    _mg_modo = int(mg_modo)
    _mg = int(martin_gale)
    _stop_gain = int(stop_gain)
    _stop_loss = int(stop_loss)
    _hora_limite = int(hora_limite)
    _minuto_limite = int(minuto_limite)  
    
    if _estrategia == "MHI2":    
     hilo1b = threading.Thread(target=mhi2, args=(_money, _par, _modo_entrada, _mg_modo, _mg, _stop_gain, _stop_loss, _hora_limite, _minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest))  
     hilo1b.start() 
     
def antesala_panel3(estrategia, money, par, modo_entrada, mg_modo, martin_gale, stop_gain, stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):

    _estrategia = str(estrategia)
    _money = int(money)
    _par = str(par)
    _modo_entrada = int(modo_entrada)
    _mg_modo = int(mg_modo)
    _mg = int(martin_gale)
    _stop_gain = int(stop_gain)
    _stop_loss = int(stop_loss)
    _hora_limite = int(hora_limite)
    _minuto_limite = int(minuto_limite)  
    
    if _estrategia == "MHI3":    
     hilo1c = threading.Thread(target=mhi3, args=(_money, _par, _modo_entrada, _mg_modo, _mg, _stop_gain, _stop_loss, _hora_limite, _minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest))  
     hilo1c.start()     
def antesala_panel4(estrategia, money, par, modo_entrada, mg_modo, martin_gale, stop_gain, stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):
    
    _estrategia = str(estrategia)
    _money = int(money)
    _par = str(par)
    _modo_entrada = int(modo_entrada)
    _mg_modo = int(mg_modo)
    _mg = int(martin_gale)
    _stop_gain = int(stop_gain)
    _stop_loss = int(stop_loss)
    _hora_limite = int(hora_limite)
    _minuto_limite = int(minuto_limite)  
    
    if _estrategia == "Torres G":    
     hilo1d = threading.Thread(target=torres, args=(_money, _par, _modo_entrada, _mg_modo, _mg, _stop_gain, _stop_loss, _hora_limite, _minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest))  
     hilo1d.start() 
     
def antesala_panel5(money,par,after_loss,mg_modo, martin_gale,martin_galaaf,num_ops_p5_,modo_entrada,stop_gain, stop_loss, hora_limite, minuto_limite,stop_ops,check_mhi,check_mhi2,check_mhi3,check_mhimai,check_mhi2mai,check_mhi3mai,check_milhaomin,check_milhaomax,check_torres,check_padrao23,check_melhor,check_padrao3x1,check_lowest,check_low,check_normal,check_high,check_highest):
    if money == "":
        ingreso_p5.insert(0, "1")
        money = "1"
    if martin_gale == "":
        mg_text_p5.insert(0, "0")
        martin_gale = "0"
        
    if num_ops_p5_ == "":
        num_ops_p5.insert(0, "1")
        num_ops_p5_ = "1"
        
    if stop_gain == "":
        stop_gain_p5.insert(0, "0")
        stop_gain = "0"
    if stop_loss == "":
        stop_loss_p5.insert(0, "0")
        stop_loss = "0"
        
    if hora_limite == "":
        limite_hora_p5.insert(0, "hs")
        hora_limite = "0"
    if minuto_limite == "":
        limite_minuto_p5.insert(0, "ms")
        minuto_limite = "0"
    if hora_limite == "hs":
        hora_limite = "0"
    if minuto_limite == "ms":
        minuto_limite = "0"    
               
    if stop_ops == "":
        stop_ops_p5.insert(0, "0")
        stop_ops = "0"    
    _money = int(money)
    _par = str(par)
    _mg_modo = int(mg_modo)
    martingalaaf = int(martin_galaaf)
    martingala = int(martin_gale)
    modoentrada = int(modo_entrada)
    _stop_gain = int(stop_gain)
    _stop_loss = int(stop_loss)
    _hora_limite = int(hora_limite)
    _minuto_limite = int(minuto_limite) 
    _stop_ops = int(stop_ops)
    _num_ops_p5 = int(num_ops_p5_)
  
    hilo_p5 = threading.Thread(target=modo_turbo, args=(_money, _par,after_loss,_mg_modo, martingala,martingalaaf,_num_ops_p5,modoentrada,_stop_gain, _stop_loss, _hora_limite, _minuto_limite,_stop_ops,check_mhi,check_mhi2,check_mhi3,check_mhimai,check_mhi2mai,check_mhi3mai,check_milhaomin,check_milhaomax,check_torres,check_padrao23,check_melhor,check_padrao3x1,check_lowest,check_low,check_normal,check_high,check_highest))  
    hilo_p5.start()
 
######################################################ESTRATEGIA MHI####################################################

def mhi(_money, par, modo_entrada, mg_modo, martingala,stop_gain, _stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):
 #try: 
  graf_panel1("Operacion Iniciada" )
                
  money = _money
  stop_loss = _stop_loss * -1
  check_status = ""
  #____________________________________________________-
  m_= 0
  ganadas1 = 0
  perdidas1 = 0
  cuenta = 0 

#___________________________________________  
  if modo_entrada == 1:
      n1=0
      n2=5
      velas = 3
  if modo_entrada == 2:
      n1=1
      n2=6
      velas = 4
  if modo_entrada == 3:
      n1=2
      n2=7
      velas = 5
  if modo_entrada == 4:
      n1=3
      n2=8
      velas = 6
  if modo_entrada == 5:
      n1=4
      n2=9   
      velas = 7
#___________________________________________
  global stop_hilo1
  stop_hilo1 = "run"
 
  while True:  
   if stop_hilo1 == "stop":  
     graf_panel1("Operacion Terminada" )
     break
 
   money = _money   
   now_ = datetime.now()
   _time_hora = format(now_.hour)
   time_hora = int(_time_hora)
   _time_minuto = format(now_.minute)
   time_minuto = int(_time_minuto)
   cuenta = ganadas1 - perdidas1
   if stop_gain != 0:
    if cuenta == stop_gain:  
      graf_panel1("Stop Gain ON" )
      break
  
   if stop_loss != 0:
    if cuenta == stop_loss:   
        graf_panel1("Stop Loose ON" )
        break
    
   if hora_limite != "0" and minuto_limite !="0":
    __hora_limite = int(hora_limite)
    __minuto_limite = int(minuto_limite)
    if __hora_limite == time_hora: 
     if __minuto_limite == time_minuto:  
         graf_panel1("Tiempo Terminado" )
         break
     
   action = ''
   mhi = 0
   mg = 0
 
   while True:
      now = datetime.now()
      seg = format(now.second)
      m = format(now.minute)
      if seg == "0": break
      time.sleep(0.5)
   m_ = int(m)
   ultimo_digito_mhi = m_ % 10
   hora_entrar_mhi = ultimo_digito_mhi
   if hora_entrar_mhi == n1 or  hora_entrar_mhi == n2:  
    if seg == '0':   
     minuto_antes = datetime.now() - timedelta(minutes=1)
     data = api.get_candles(par, 60, velas, datetime.timestamp(minuto_antes))
     
      
     if data[0]['open'] < data[0]['close']: 
      vela0 = 1 
     else:
      if data[0]['open'] > data[0]['close']: 
       vela0 = -1
      else: vela0 = 0     
      
     if data[1]['open'] < data[1]['close']: 
      vela1 = 1 
     else:
      if data[1]['open'] > data[1]['close']: 
       vela1 = -1
      else: vela1 = 0
      
     if data[2]['open'] < data[2]['close']: 
      vela2 = 1 
     else:
      if data[2]['open'] > data[2]['close']: 
        vela2 = -1
      else: vela2 = 0
      
     if modo_entrada >= 2:
      if data[3]['open'] < data[3]['close']: 
       vela3 = 1 
      else:
       if data[3]['open'] > data[3]['close']: 
        vela3 = -1
       else: vela3 = 0
        
     if modo_entrada >= 3:
      if data[4]['open'] < data[4]['close']: 
       vela4 = 1 
      else:
       if data[4]['open'] > data[4]['close']: 
        vela4 = -1
       else: vela4 = 0
       
     if modo_entrada >= 4:
      if data[5]['open'] < data[5]['close']: 
       vela5 = 1 
      else:
       if data[5]['open'] > data[5]['close']: 
        vela5 = -1
       else: vela5 = 0
       
     if modo_entrada >= 5:
      if data[6]['open'] < data[6]['close']: 
       vela6 = 1 
      else:
       if data[6]['open'] > data[6]['close']: 
        vela6 = -1
       else: vela6 = 0
      
     if vela0 == 0 or vela1 == 0 or vela2 == 0: 
       doji = "true" 
       graf_panel1("Doji encontrado" )
     else: doji = "false"
         
     mhi = vela0 + vela1 + vela2
     
     if modo_entrada == 1 and doji == "false":
      if mhi > 0:
          action = 'put'
      if mhi < 0:
          action = 'call' 
          
     if modo_entrada == 2 and doji == "false":
      mg = vela3
      if vela3 == 0:  
          graf_panel1("Doji encontrado" )
      if mhi > 0 and mg == 1:
          action = 'put'
      if mhi < 0 and mg ==-1:
          action = 'call'
          
     if modo_entrada == 3 and doji == "false":
      if vela3 == 0 or vela4 == 0:   
           graf_panel1("Doji encontrado" )
      mg = vela3 + vela4
      if mhi > 0 and mg ==2:
          action = 'put'
      if mhi < 0 and mg ==-2:
          action = 'call'  
          
     if modo_entrada == 4 and doji == "false":
      if vela3 == 0 or vela4 == 0 or vela5 == 0:    
           graf_panel1("Doji encontrado" )
       
      mg = vela3 + vela4 + vela5
      if mhi > 0 and mg ==3:
          action = 'put'
      if mhi < 0 and mg ==-3:
          action = 'call'  
          
     if modo_entrada == 5 and doji == "false":
      if vela3 == 0 or vela4 == 0 or vela5 == 0 or vela6 ==0:   
           graf_panel1("Doji encontrado" )
     
      mg = vela3 + vela4 + vela5 + vela6
      if mhi > 0 and mg ==4:
         action = 'put'
      if mhi < 0 and mg ==-4:
         action = 'call'  
      
    
    #########################################################################################################################   
     mg_stop=0
     
     if action == "put" or action == "call":
      while True:
       if stop_hilo1 == "stop":
         graf_panel1("Operacion Terminada"  )
         break
       
       if mg_stop > martingala: 
        perdidas1 = perdidas1 + 1   
        graf_panel1_score(ganadas1,perdidas1)
        graf_global()
        ganancias_totales(check_status)
        break
    
       check,id1 = api.buy(money,par,action,1)
       
       if check:  
           if action == "put": graf_panel1("Venta Realizada" )
           if action == "put": graf_panel1("Venta Realizada" )
           start_time_remaning_p1()
       else:  
           graf_panel1("Asset no disponible" ) 
           break
###############################################################################################################       
       try:
         check_status = api.check_win_v4(id1)
       except:   
         graf_panel1("error" )
         
    
       if check_status[0] == "win": 
         ganadas1 = ganadas1 + 1
         graf_panel1_score(ganadas1,perdidas1)
         graf_global()
         ganancias_totales(check_status)  
         graf_panel1("Operacion Win")
         break
       else:
         if check_status[0] == "loose": 
          graf_panel1("Operacion Loose")
          global profit1      
          if mg_modo == 0:
           plus = 2 + profit1
          if mg_modo == 1:
           plus = 1 + profit1
          money = money *  plus
         else:
           graf_panel1("Operacion Equal")
           break
       
       mg_stop = mg_stop + 1 
       time.sleep(0.5)
   time.sleep(0.5)  
 #except:   
    #graf_panel1("Error en operacion")
    
def mhi2(_money, par, modo_entrada, mg_modo, martingala,stop_gain, _stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):
 #try: 
  graf_panel2("Operacion Iniciada" )
                
  money = _money
  stop_loss = _stop_loss * -1
  check_status = ""
  #____________________________________________________-
  m_= 0
  ganadas1 = 0
  perdidas1 = 0
  cuenta = 0 

#___________________________________________  
  if modo_entrada == 1:
      n1=1
      n2=6
      velas = 4
  if modo_entrada == 2:
      n1=2
      n2=7
      velas = 5
  if modo_entrada == 3:
      n1=3
      n2=8
      velas = 6
  if modo_entrada == 4:
      n1=4
      n2=9
      velas = 7
  if modo_entrada == 5:
      n1=0
      n2=5   
      velas = 8
#___________________________________________
  global stop_hilo2
  stop_hilo2 = "run"
 
  while True:    
   if stop_hilo2 == "stop":  
     graf_panel2("Operacion Terminada" )
     break
   time.sleep(0.1)
   
   money = _money   
   now_ = datetime.now()
   _time_hora = format(now_.hour)
   time_hora = int(_time_hora)
   _time_minuto = format(now_.minute)
   time_minuto = int(_time_minuto)
   cuenta = ganadas1 - perdidas1
   if stop_gain != 0:
    if cuenta == stop_gain:  
      graf_panel2("Stop Gain ON" )
      break
  
   if stop_loss != 0:
    if cuenta == stop_loss:   
        graf_panel2("Stop Loose ON" )
        break
    
   if hora_limite != "0" and minuto_limite !="0":
    __hora_limite = int(hora_limite)
    __minuto_limite = int(minuto_limite)
    if __hora_limite == time_hora: 
     if __minuto_limite == time_minuto:  
         graf_panel2("Tiempo Terminado" )
         break
     
   action = ''
   mhi = 0
   mg = 0
  
   while True:
    now = datetime.now()
    seg = format(now.second)
    m = format(now.minute)
    if seg=="0": break
   
   m_ = int(m)
   ultimo_digito_mhi = m_ % 10;
   hora_entrar_mhi = ultimo_digito_mhi
   if hora_entrar_mhi == n1 or  hora_entrar_mhi == n2:
    if seg == '0':   
     minuto_antes = datetime.now() - timedelta(minutes=1)
     data = api.get_candles(par, 60, velas, datetime.timestamp(minuto_antes))
         
     if data[0]['open'] < data[0]['close']: 
      vela0 = 1 
     else:
      if data[0]['open'] > data[0]['close']: 
       vela0 = -1
      else: vela0 = 0     
      
     if data[1]['open'] < data[1]['close']: 
      vela1 = 1 
     else:
      if data[1]['open'] > data[1]['close']: 
       vela1 = -1
      else: vela1 = 0
      
     if data[2]['open'] < data[2]['close']: 
      vela2 = 1 
     else:
      if data[2]['open'] > data[2]['close']: 
        vela2 = -1
      else: vela2 = 0
     
     if data[3]['open'] < data[3]['close']: 
       vela3 = 1 
     else:
      if data[3]['open'] > data[3]['close']: 
        vela3 = -1
      else: vela3 = 0
       
     if modo_entrada >= 2:
      if data[4]['open'] < data[4]['close']: 
       vela4 = 1 
      else:
       if data[4]['open'] > data[4]['close']: 
        vela4 = -1
       else: vela4 = 0
        
     if modo_entrada >= 3:
      if data[5]['open'] < data[5]['close']: 
       vela5 = 1 
      else:
       if data[5]['open'] > data[5]['close']: 
        vela5 = -1
       else: vela5 = 0
       
     if modo_entrada >= 4:
      if data[6]['open'] < data[6]['close']: 
       vela6 = 1 
      else:
       if data[6]['open'] > data[6]['close']: 
        vela6 = -1
       else: vela6 = 0
       
     if modo_entrada >= 5:
      if data[7]['open'] < data[7]['close']: 
       vela7 = 1 
      else:
       if data[7]['open'] > data[7]['close']: 
        vela7 = -1
       else: vela7 = 0
      
     if vela0 == 0 or vela1 == 0 or vela2 == 0: 
       doji = "true" 
       graf_panel2("Doji encontrado" )
     else: doji = "false"
         
     mhi = vela0 + vela1 + vela2
     
     if modo_entrada == 1 and doji == "false":
      if mhi > 0:
          action = 'put'
      if mhi < 0:
          action = 'call' 
          
     if modo_entrada == 2 and doji == "false":
      mg = vela4
      if vela4 == 0:  
          graf_panel2("Doji encontrado" )
      if mhi > 0 and mg == 1:
          action = 'put'
      if mhi < 0 and mg ==-1:
          action = 'call'
          
     if modo_entrada == 3 and doji == "false":
      if vela4 == 0 or vela5 == 0:   
           graf_panel2("Doji encontrado" )
      mg = vela4 + vela5
      if mhi > 0 and mg ==2:
          action = 'put'
      if mhi < 0 and mg ==-2:
          action = 'call'  
          
     if modo_entrada == 4 and doji == "false":
      if vela4 == 0 or vela5 == 0 or vela6 == 0:    
           graf_panel2("Doji encontrado" )
       
      mg = vela4 + vela5 + vela6
      if mhi > 0 and mg ==3:
          action = 'put'
      if mhi < 0 and mg ==-3:
          action = 'call'  
          
     if modo_entrada == 5 and doji == "false":
      if vela4 == 0 or vela5 == 0 or vela6 == 0 or vela7 ==0:   
           graf_panel2("Doji encontrado" )
     
      mg = vela4 + vela5 + vela6 + vela7
      if mhi > 0 and mg ==4:
         action = 'put'
      if mhi < 0 and mg ==-4:
         action = 'call'  
      
    
    #########################################################################################################################   
     mg_stop=0
     
     if action == "put" or action == "call":
      while True:
       if stop_hilo1 == "stop":
         graf_panel2("Operacion Terminada"  )
         break
      
       if mg_stop > martingala: 
        perdidas1 = perdidas1 + 1   
        graf_panel2_score(ganadas1,perdidas1)
        graf_global()
        ganancias_totales(check_status)
        break

       check,id1 = api.buy(money,par,action,1)
       
       if check:  
           if action == "put": graf_panel2("Venta Realizada" )
           if action == "call": graf_panel2("Compra Realizada" )
           start_time_remaning_p2()
       else:  
           graf_panel2("Asset no disponible" ) 
           break
###############################################################################################################       
       try:
         check_status = api.check_win_v4(id1)
       except:   
         graf_panel2("error" )
         
    
       if check_status[0] == "win": 
         ganadas1 = ganadas1 + 1
         
         graf_panel2_score(ganadas1,perdidas1)
         graf_global()
         ganancias_totales(check_status)  
         graf_panel2("Operacion Win")
         break
     
       else:
         if check_status[0] == "loose": 
          graf_panel2("Operacion Loose")
          global profit2       
          if mg_modo == 0:
           plus = 2 + profit2
          if mg_modo == 1:
           plus = 1 + profit2
          money = money *  plus
          
         else:
           graf_panel2("Operacion Equal")
           break
        
       mg_stop = mg_stop + 1 
      
 #except:   
    #graf_panel2("Error en operacion")   
   
def mhi3(_money, par, modo_entrada, mg_modo, martingala,stop_gain, _stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):
 #try: 
  graf_panel3("Operacion Iniciada" )
                
  money = _money
  stop_loss = _stop_loss * -1
  check_status = ""
  #____________________________________________________-
  m_= 0
  ganadas1 = 0
  perdidas1 = 0
  cuenta = 0 

#___________________________________________  
  if modo_entrada == 1:
      n1=2
      n2=7
      velas = 5
  if modo_entrada == 2:
      n1=3
      n2=8
      velas = 6
  if modo_entrada == 3:
      n1=4
      n2=9
      velas = 7
  if modo_entrada == 4:
      n1=0
      n2=5
      velas = 8
  if modo_entrada == 5:
      n1=1
      n2=6   
      velas = 9
#___________________________________________
  global stop_hilo3
  stop_hilo3 = "run"
 
  while True:    
   if stop_hilo3 == "stop":  
     graf_panel3("Operacion Terminada" )
     break
 
   money = _money   
   now_ = datetime.now()
   _time_hora = format(now_.hour)
   time_hora = int(_time_hora)
   _time_minuto = format(now_.minute)
   time_minuto = int(_time_minuto)
   cuenta = ganadas1 - perdidas1
   if stop_gain != 0:
    if cuenta == stop_gain:  
      graf_panel3("Stop Gain ON" )
      break
  
   if stop_loss != 0:
    if cuenta == stop_loss:   
        graf_panel3("Stop Loose ON" )
        break
    
   if hora_limite != "0" and minuto_limite !="0":
    __hora_limite = int(hora_limite)
    __minuto_limite = int(minuto_limite)
    if __hora_limite == time_hora: 
     if __minuto_limite == time_minuto:  
         graf_panel3("Tiempo Terminado" )
         break
     
   action = ''
   mhi = 0
   mg = 0
   while True:
    now = datetime.now()
    seg = format(now.second)
    m = format(now.minute)
    if seg == "0": break
        
   m_ = int(m)
   ultimo_digito_mhi = m_ % 10;
   hora_entrar_mhi = ultimo_digito_mhi
   if hora_entrar_mhi == n1 or  hora_entrar_mhi == n2:
    if seg == '0':   
     minuto_antes = datetime.now() - timedelta(minutes=1)
     data = api.get_candles(par, 60, velas, datetime.timestamp(minuto_antes))
     
      
     if data[0]['open'] < data[0]['close']: 
      vela0 = 1 
     else:
      if data[0]['open'] > data[0]['close']: 
       vela0 = -1
      else: vela0 = 0     
      
     if data[1]['open'] < data[1]['close']: 
      vela1 = 1 
     else:
      if data[1]['open'] > data[1]['close']: 
       vela1 = -1
      else: vela1 = 0
      
     if data[2]['open'] < data[2]['close']: 
      vela2 = 1 
     else:
      if data[2]['open'] > data[2]['close']: 
        vela2 = -1
      else: vela2 = 0
     
     if data[3]['open'] < data[3]['close']: 
       vela3 = 1 
     else:
      if data[3]['open'] > data[3]['close']: 
        vela3 = -1
      else: vela3 = 0
     
     if data[4]['open'] < data[4]['close']: 
      vela4 = 1 
     else:
      if data[4]['open'] > data[4]['close']: 
       vela4 = -1
      else: vela4 = 0
        
     if modo_entrada >= 2:
      if data[5]['open'] < data[5]['close']: 
       vela5 = 1 
      else:
       if data[5]['open'] > data[5]['close']: 
        vela5 = -1
       else: vela5 = 0
       
     if modo_entrada >= 3:
      if data[6]['open'] < data[6]['close']: 
       vela6 = 1 
      else:
       if data[6]['open'] > data[6]['close']: 
        vela6 = -1
       else: vela6 = 0
       
     if modo_entrada >= 4:
      if data[7]['open'] < data[7]['close']: 
       vela7 = 1 
      else:
       if data[7]['open'] > data[7]['close']: 
        vela7 = -1
       else: vela7 = 0
       
     if modo_entrada >= 5:
      if data[8]['open'] < data[8]['close']: 
       vela8 = 1 
      else:
       if data[8]['open'] > data[8]['close']: 
        vela8 = -1
       else: vela8 = 0
       
     if vela0 == 0 or vela1 == 0 or vela2 == 0: 
       doji = "true" 
       graf_panel3("Doji encontrado" )
     else: doji = "false"
         
     mhi = vela0 + vela1 + vela2
     
     if modo_entrada == 1 and doji == "false":
      if mhi > 0:
          action = 'put'
      if mhi < 0:
          action = 'call' 
          
     if modo_entrada == 2 and doji == "false":
      mg = vela5
      if vela5 == 0:  
          graf_panel3("Doji encontrado" )
      if mhi > 0 and mg == 1:
          action = 'put'
      if mhi < 0 and mg ==-1:
          action = 'call'
          
     if modo_entrada == 3 and doji == "false":
      if vela5 == 0 or vela6 == 0:   
           graf_panel3("Doji encontrado" )
      mg = vela5 + vela6
      if mhi > 0 and mg ==2:
          action = 'put'
      if mhi < 0 and mg ==-2:
          action = 'call'  
          
     if modo_entrada == 4 and doji == "false":
      if vela5 == 0 or vela6 == 0 or vela7 == 0:    
           graf_panel3("Doji encontrado" )
       
      mg = vela5 + vela6 + vela7
      if mhi > 0 and mg ==3:
          action = 'put'
      if mhi < 0 and mg ==-3:
          action = 'call'  
          
     if modo_entrada == 5 and doji == "false":
      if vela5 == 0 or vela6 == 0 or vela7 == 0 or vela8 ==0:   
           graf_panel3("Doji encontrado" )
     
      mg = vela5 + vela6 + vela7 + vela8
      if mhi > 0 and mg ==4:
         action = 'put'
      if mhi < 0 and mg ==-4:
         action = 'call'  
      
    
    #########################################################################################################################   
     mg_stop=0
     
     if action == "put" or action == "call":
      while True:
       if stop_hilo1 == "stop":
         graf_panel3("Operacion Terminada"  )
         break
      
       if mg_stop > martingala: 
        perdidas1 = perdidas1 + 1   
        graf_panel3_score(ganadas1,perdidas1)
        graf_global()
        ganancias_totales(check_status)
        break

       check,id1 = api.buy(money,par,action,1)
       
       if check:  
           if action == "put": graf_panel3("Venta Realizada" )
           if action == "call": graf_panel3("Compra Realizada" )
           start_time_remaning_p3()
       else:  
           graf_panel3("Asset no disponible" ) 
           break
###############################################################################################################       
       try:
         check_status = api.check_win_v4(id1)
       except:   
         graf_panel3("error" )
         
    
       if check_status[0] == "win": 
         ganadas1 = ganadas1 + 1
         
         graf_panel3_score(ganadas1,perdidas1)
         graf_global()
         ganancias_totales(check_status)  
         graf_panel3("Operacion Win")
       
      
         break
       else:
         if check_status[0] == "loose": 
          graf_panel3("Operacion Loose")
          global profit2       
          if mg_modo == 0:
           plus = 2 + profit3
          if mg_modo == 1:
           plus = 1 + profit3
          money = money *  plus
          
         else:
           graf_panel3("Operacion Equal")
           break
    
       mg_stop = mg_stop + 1 

      
 #except:   
    #graf_panel3("Error en operacion") 
    
def torres(_money, par, modo_entrada, mg_modo, martingala,stop_gain, _stop_loss, hora_limite, minuto_limite,check_lowest,check_low,check_normal,check_high,check_highest):
 #try: 
  graf_panel4("Operacion Iniciada" )
                
  money = _money
  stop_loss = _stop_loss * -1
  check_status = ""
  #____________________________________________________-
  m_= 0
  ganadas1 = 0
  perdidas1 = 0
  cuenta = 0 

#___________________________________________  
  if modo_entrada == 1:
      n1=4
      n2=9
      velas = 4
  if modo_entrada == 2:
      n1=0
      n2=5
      velas = 5
  if modo_entrada == 3:
      n1=1
      n2=6
      velas = 6
  if modo_entrada == 4:
      n1=2
      n2=7
      velas = 7
  if modo_entrada == 5:
      n1=3
      n2=8   
      velas = 8
#___________________________________________
  global stop_hilo4
  stop_hilo4 = "run"
 
  while True:  
   if stop_hilo4 == "stop":  
     graf_panel4("Operacion Terminada" )
     break
 
   money = _money   
   now_ = datetime.now()
   _time_hora = format(now_.hour)
   time_hora = int(_time_hora)
   _time_minuto = format(now_.minute)
   time_minuto = int(_time_minuto)
   cuenta = ganadas1 - perdidas1
   if stop_gain != 0:
    if cuenta == stop_gain:  
      graf_panel4("Stop Gain ON" )
      break
  
   if stop_loss != 0:
    if cuenta == stop_loss:   
        graf_panel4("Stop Loose ON" )
        break
    
   if hora_limite != "0" and minuto_limite !="0":
    __hora_limite = int(hora_limite)
    __minuto_limite = int(minuto_limite)
    if __hora_limite == time_hora: 
     if __minuto_limite == time_minuto:  
         graf_panel4("Tiempo Terminado" )
         break
     
   action = ''
   mhi = 0
   mg = 0
   while True:
    now = datetime.now()
    seg = format(now.second)
    m = format(now.minute)
    if seg == "0": break
        
   m_ = int(m)
   ultimo_digito_mhi = m_ % 10;
   hora_entrar_mhi = ultimo_digito_mhi
   if hora_entrar_mhi == n1 or  hora_entrar_mhi == n2:
    if seg == '0':   
     minuto_antes = datetime.now() - timedelta(minutes=1)
     data = api.get_candles(par, 60, velas, datetime.timestamp(minuto_antes))
     
      
     if data[0]['open'] < data[0]['close']: 
      vela0 = 1 
     else:
      if data[0]['open'] > data[0]['close']: 
       vela0 = -1
      else: vela0 = 0     
      
     if data[1]['open'] < data[1]['close']: 
      vela1 = 1 
     else:
      if data[1]['open'] > data[1]['close']: 
       vela1 = -1
      else: vela1 = 0
      
     if data[2]['open'] < data[2]['close']: 
      vela2 = 1 
     else:
      if data[2]['open'] > data[2]['close']: 
        vela2 = -1
      else: vela2 = 0
     
     if data[3]['open'] < data[3]['close']: 
       vela3 = 1 
     else:
      if data[3]['open'] > data[3]['close']: 
        vela3 = -1
      else: vela3 = 0
       
     if modo_entrada >= 2:
      if data[4]['open'] < data[4]['close']: 
       vela4 = 1 
      else:
       if data[4]['open'] > data[4]['close']: 
        vela4 = -1
       else: vela4 = 0
        
     if modo_entrada >= 3:
      if data[5]['open'] < data[5]['close']: 
       vela5 = 1 
      else:
       if data[5]['open'] > data[5]['close']: 
        vela5 = -1
       else: vela5 = 0
       
     if modo_entrada >= 4:
      if data[6]['open'] < data[6]['close']: 
       vela6 = 1 
      else:
       if data[6]['open'] > data[6]['close']: 
        vela6 = -1
       else: vela6 = 0
       
     if modo_entrada >= 5:
      if data[7]['open'] < data[7]['close']: 
       vela7 = 1 
      else:
       if data[7]['open'] > data[7]['close']: 
        vela7 = -1
       else: vela7 = 0
      
        
     if vela0 == 0: 
       doji = "true" 
       graf_panel4("Doji encontrado" )
     else: doji = "false"
         
     mhi = vela0
     
     if modo_entrada == 1 and doji == "false":
      if mhi < 0:
          action = 'put'
      if mhi > 0:
          action = 'call' 
          
     if modo_entrada == 2 and doji == "false":
      mg = vela4
      if vela4 == 0:  
          graf_panel4("Doji encontrado" )
      if mhi < 0 and mg == 1:
          action = 'put'
      if mhi > 0 and mg ==-1:
          action = 'call'
          
     if modo_entrada == 3 and doji == "false":
      if vela4 == 0 or vela5 == 0:   
           graf_panel4("Doji encontrado" )
      mg = vela4 + vela5
      if mhi < 0 and mg ==2:
          action = 'put'
      if mhi > 0 and mg ==-2:
          action = 'call'  
          
     if modo_entrada == 4 and doji == "false":
      if vela4 == 0 or vela5 == 0 or vela6 == 0:    
           graf_panel4("Doji encontrado" )
       
      mg = vela4 + vela5 + vela6
      if mhi < 0 and mg ==3:
          action = 'put'
      if mhi > 0 and mg ==-3:
          action = 'call'  
          
     if modo_entrada == 5 and doji == "false":
      if vela4 == 0 or vela5 == 0 or vela6 == 0 or vela7 ==0:   
           graf_panel4("Doji encontrado" )
     
      mg = vela4 + vela5 + vela6 + vela7
      if mhi < 0 and mg ==4:
         action = 'put'
      if mhi > 0 and mg ==-4:
         action = 'call'  
      
    
    #########################################################################################################################   
     mg_stop=0
     
     if action == "put" or action == "call":
      while True:
       if stop_hilo4 == "stop":
         graf_panel4("Operacion Terminada"  )
         break
      
       if mg_stop > martingala: 
        perdidas1 = perdidas1 + 1   
        graf_panel4_score(ganadas1,perdidas1)
        graf_global()
        ganancias_totales(check_status)
        break

       check,id1 = api.buy(money,par,action,1)
       
       if check:  
           if action == "put": graf_panel4("Venta Realizada" )
           if action == "call": graf_panel4("Compra Realizada" )
           start_time_remaning_p4()
       else:  
           graf_panel4("Asset no disponible" ) 
           break
###############################################################################################################       
       try:
         check_status = api.check_win_v4(id1)
       except:   
         graf_panel4("error" )
         
    
       if check_status[0] == "win": 
         ganadas1 = ganadas1 + 1
         
         graf_panel4_score(ganadas1,perdidas1)
         graf_global()
         ganancias_totales(check_status)  
         graf_panel4("Operacion Win")
       
      
         break
       else:
         if check_status[0] == "loose": 
          graf_panel4("Operacion Loose")
          global profit4       
          if mg_modo == 0:
           plus = 2 + profit4
          if mg_modo == 1:
           plus = 1 + profit4
          money = money *  plus
          
         else:
           graf_panel4("Operacion Equal")
           break
    
       mg_stop = mg_stop + 1 
      
      
 #except:   
    #graf_panel2("Error en operacion")




def modo_turbo(_money, par,after_loss, mg_modo, martingala,martingalaaf,_num_ops_p5,modo_entrada, stop_gain, _stop_loss, hora_limite, minuto_limite,stop_ops,check_mhi,check_mhi2,check_mhi3,check_mhimai,check_mhi2mai,check_mhi3mai,check_milhaomin,check_milhaomax,check_torres,check_padrao23,check_melhor,check_padrao3x1,check_lowest,check_low,check_normal,check_high,check_highest):
  
  graf_panel5("Operacion Iniciada" )                   
  stop_loss = _stop_loss * -1
  check_status = ""
  global estado
  #____________________________________________________-
  m_= 0
  ganadas1 = 0
  perdidas1 = 0
  cuenta = 0 
  clave = 0
  count_mhi = 0
  estado = "desbloquiado"
#_______________________
  global t_final
  global minu_5
  global hora_5
  global n_operaciones
  t_final = 0
  global stop_hilo5
  stop_hilo5 = "run"
  n_operaciones = 0
  romper = 0
  while True:   
   action = ""
   data_turbo = []
   
   n = 0
   n2 = 0
   n3 = 0
   n4 = 0
   
   if modo_entrada == 1:
       n1 = 0
       n2 = 0
       n3 = 0
       n4 = 0 
   if modo_entrada == 2: 
       n1 = 1
       n2 = 1
       n3 = 1
       n4 = -4 
   if modo_entrada == 3:
       n1 = 2
       n2 = 2
       n3 = 2
       n4 = -3
   if modo_entrada == 4: 
       n1 = 3
       n2 = 3
       n3 = -2
       n4 = -2
   if modo_entrada == 5: 
       n1 = 4
       n2 = -1
       n3 = -1
       n4 = -1
   analisis_tecnico = "none"
   while True:
      if stop_hilo5 == "stop":
       graf_panel5("Operacion Terminada" )
       romper = 1
       break
     
      if stop_gain != 0:
       if t_final >= stop_gain:
        graf_panel5("Stop Gain ON" )
        romper = 1
        break
      if stop_loss != 0:  
       if t_final <= stop_loss: 
           graf_panel5("Stop Loss ON" )
           romper = 1
           break
      if hora_limite != 0 or minuto_limite != 0:
       if hora_limite <= hora_5: 
        if minuto_limite <= minu_5: 
            graf_panel5("Tiempo Terminado" )
            romper = 1
            break 
      if stop_ops != 0:
       if n_operaciones >= stop_ops:
        graf_panel5("Stop Ops ON" )
        romper = 1
        break
    
      now = datetime.now()
      seg2 = format(now.second)
      if seg2 == "56": 
          break
      time.sleep(0.5)
   if romper == 1:
       break
   if check_lowest == 1 or check_low == 1 or check_normal == 1 or check_high == 1 or check_highest == 1:  
    if seg2 == "56":
       indicators = api.get_technical_indicators(par)
       n_indi = 0
       buy_count = 0
       sell_count = 0
       hold_count = 0
       while n_indi < 57:
        
        action = indicators[n_indi]["action"] 
        if action == "sell": sell_count = sell_count + 1
        if action == "buy": buy_count = buy_count + 1
        if action == "hold": hold_count = hold_count + 1
        n_indi = n_indi + 1    
            
     ############################## VERY LOW #################################

       if check_lowest == 1: 
       
           if sell_count > buy_count:
            analisis_tecnico = "venta"
           else:
            if buy_count > sell_count:
             analisis_tecnico = "compra"
            else:
              analisis_tecnico = "none" 
             
     ############################## LOW ######################################
       if check_low == 1:
           
           if sell_count > buy_count and sell_count >= 5:
            analisis_tecnico = "venta"
           else:
            if buy_count > sell_count and buy_count >= 5:
             analisis_tecnico = "compra"
            else: analisis_tecnico = "none"   
        
     ############################## NORMAL ######################################
       if check_normal == 1:
       
           if sell_count > buy_count and sell_count >= 10:
            analisis_tecnico = "venta"
           else:
            if buy_count > sell_count and buy_count >= 10:
             analisis_tecnico = "compra"
            else: analisis_tecnico = "none"   

     ############################## HIGH ######################################
       if check_high == 1:
       
           if sell_count > buy_count and sell_count >= 15:
            analisis_tecnico = "venta"
           else:
            if buy_count > sell_count and buy_count >= 15:
             analisis_tecnico = "compra"
            else: analisis_tecnico = "none"   
          
     ############################## VERY HIGH ######################################
       if check_highest == 1:
           if sell_count > buy_count and sell_count >= 20:
            analisis_tecnico = "venta"
           else:
            if buy_count > sell_count and buy_count >= 20:
             analisis_tecnico = "compra"
            else: analisis_tecnico = "none"
         
   while True:
       now = datetime.now()
       seg = format(now.second)
       m = format(now.minute)
       if seg == "0": 
           break
       time.sleep(0.1)
   velas = 0
   m_ = int(m)
   ultimo_digito_mhi = m_ % 10;
   hora_entrar_mhi = ultimo_digito_mhi    
        
   if hora_entrar_mhi == 0 + n1 or  hora_entrar_mhi == 5 + n1:
    velas = 20 + n1  
   if hora_entrar_mhi == 1 + n2 or  hora_entrar_mhi == 6 + n2:
    velas = 21 + n1  
   if hora_entrar_mhi == 2 + n3 or  hora_entrar_mhi == 7 + n3:
    velas = 22 + n1
   if hora_entrar_mhi == 4 + n4 or  hora_entrar_mhi == 9 + n4:
    velas = 19 + n1
    
   count_data_turbo = 0 
   if hora_entrar_mhi == 0 or  hora_entrar_mhi == 5 or hora_entrar_mhi == 1 or  hora_entrar_mhi == 6 or hora_entrar_mhi == 2 or  hora_entrar_mhi == 7 or hora_entrar_mhi == 4 or  hora_entrar_mhi == 9:
    if seg == "0":   
      money = _money 
      minuto_antes = datetime.now() - timedelta(minutes=1)
      data_turbo = api.get_candles(par, 60, velas, datetime.timestamp(minuto_antes))
      count_data_turbo = len(data_turbo)
      vela19 = 0 
      vela20 = 0
      vela21 = 0
      vela22 = 0
      vela23 = 0
      vela24 = 0 
      vela25 = 0
     
      if data_turbo[0]['open'] < data_turbo[0]['close']: 
       vela0 = 1 
      else:
       if data_turbo[0]['open'] > data_turbo[0]['close']: 
        vela0 = -1
       else: vela0 = 0     
       
      if data_turbo[1]['open'] < data_turbo[1]['close']: 
       vela1 = 1 
      else:
       if data_turbo[1]['open'] > data_turbo[1]['close']: 
        vela1 = -1
       else: vela1 = 0
       
      if data_turbo[2]['open'] < data_turbo[2]['close']: 
       vela2 = 1 
      else:
       if data_turbo[2]['open'] > data_turbo[2]['close']: 
        vela2 = -1
       else: vela2 = 0
       
      if data_turbo[3]['open'] < data_turbo[3]['close']: 
       vela3 = 1 
      else:
       if data_turbo[3]['open'] > data_turbo[3]['close']: 
        vela3 = -1
       else: vela3 = 0     
       
      if data_turbo[4]['open'] < data_turbo[4]['close']: 
       vela4 = 1 
      else:
       if data_turbo[4]['open'] > data_turbo[4]['close']: 
        vela4 = -1
       else: vela4 = 0
       
      if data_turbo[5]['open'] < data_turbo[5]['close']: 
       vela5 = 1 
      else:
       if data_turbo[5]['open'] > data_turbo[5]['close']: 
        vela5 = -1
       else: vela5 = 0
      
      if data_turbo[6]['open'] < data_turbo[6]['close']: 
       vela6 = 1 
      else:
       if data_turbo[6]['open'] > data_turbo[6]['close']: 
        vela6 = -1
       else: vela6 = 0     
       
      if data_turbo[7]['open'] < data_turbo[7]['close']: 
       vela7 = 1 
      else:
       if data_turbo[7]['open'] > data_turbo[7]['close']: 
        vela7 = -1
       else: vela7 = 0
       
      if data_turbo[8]['open'] < data_turbo[8]['close']: 
       vela8 = 1 
      else:
       if data_turbo[8]['open'] > data_turbo[8]['close']: 
        vela8 = -1
       else: vela8 = 0
       
      if data_turbo[9]['open'] < data_turbo[9]['close']: 
       vela9 = 1 
      else:
       if data_turbo[9]['open'] > data_turbo[9]['close']: 
        vela9 = -1
       else: vela9 = 0     
       
      if data_turbo[10]['open'] < data_turbo[10]['close']: 
       vela10 = 1 
      else:
       if data_turbo[10]['open'] > data_turbo[10]['close']: 
        vela10 = -1
       else: vela10 = 0
       
      if data_turbo[11]['open'] < data_turbo[11]['close']: 
       vela11 = 1 
      else:
       if data_turbo[11]['open'] > data_turbo[11]['close']: 
        vela11 = -1
       else: vela11 = 0
       
      if data_turbo[12]['open'] < data_turbo[12]['close']: 
       vela12 = 1 
      else:
       if data_turbo[12]['open'] > data_turbo[12]['close']: 
        vela12 = -1
       else: vela12 = 0     
      
      if data_turbo[13]['open'] < data_turbo[13]['close']: 
       vela13 = 1 
      else:
       if data_turbo[13]['open'] > data_turbo[13]['close']: 
        vela13 = -1
       else: vela13 = 0
      
      if data_turbo[14]['open'] < data_turbo[14]['close']: 
       vela14 = 1 
      else:
       if data_turbo[14]['open'] > data_turbo[14]['close']: 
        vela14 = -1
       else: vela14 = 0
      
      if data_turbo[15]['open'] < data_turbo[15]['close']: 
       vela15 = 1 
      else:
       if data_turbo[15]['open'] > data_turbo[15]['close']: 
        vela15 = -1
       else: vela15 = 0
      
      if data_turbo[16]['open'] < data_turbo[16]['close']: 
       vela16 = 1 
      else:
       if data_turbo[16]['open'] > data_turbo[16]['close']: 
        vela16 = -1
       else: vela16 = 0
      
      if data_turbo[17]['open'] < data_turbo[17]['close']: 
       vela17 = 1 
      else:
       if data_turbo[17]['open'] > data_turbo[17]['close']: 
        vela17 = -1
       else: vela17 = 0     
     
      if data_turbo[18]['open'] < data_turbo[18]['close']: 
       vela18 = 1 
      else:
       if data_turbo[18]['open'] > data_turbo[18]['close']: 
        vela18 = -1
       else: vela18 = 0
      if count_data_turbo >= 20:
       if data_turbo[19]['open'] < data_turbo[19]['close']: 
         vela19 = 1 
       else:
        if data_turbo[19]['open'] > data_turbo[19]['close']: 
         vela19 = -1
        else: vela19 = 0  
          
      if count_data_turbo >= 21:   
       if data_turbo[20]['open'] < data_turbo[20]['close']: 
        vela20 = 1 
       else:
        if data_turbo[20]['open'] > data_turbo[20]['close']: 
         vela20 = -1
        else: vela20 = 0  
        
      if count_data_turbo >= 22:   
       if data_turbo[21]['open'] < data_turbo[21]['close']: 
        vela21 = 1 
       else:
        if data_turbo[21]['open'] > data_turbo[21]['close']: 
         vela21 = -1
        else: vela21 = 0 
      
      if count_data_turbo >= 23:
       if data_turbo[22]['open'] < data_turbo[22]['close']: 
        vela22 = 1 
       else:
         if data_turbo[22]['open'] > data_turbo[22]['close']: 
          vela22 = -1
         else: vela22 = 0

      if count_data_turbo >= 24:
       if data_turbo[23]['open'] < data_turbo[23]['close']: 
         vela23 = 1 
       else:
        if data_turbo[23]['open'] > data_turbo[23]['close']: 
         vela23 = -1
        else: vela23 = 0 
     
      if count_data_turbo >= 25:
       if data_turbo[24]['open'] < data_turbo[24]['close']: 
        vela24 = 1 
       else:
        if data_turbo[24]['open'] > data_turbo[24]['close']: 
          vela24 = -1
        else: vela24 = 0    
  
      if count_data_turbo >= 26:
       if data_turbo[25]['open'] < data_turbo[25]['close']: 
        vela25 = 1 
       else:
         if data_turbo[25]['open'] > data_turbo[25]['close']: 
          vela25 = -1
         else: vela25 = 0 
              
     
      mhi_af1 = vela2 + vela3 + vela4
      mhi_af2 = vela7 + vela8 + vela9   
      mhi_af3 = vela12 + vela13 + vela14 
      
      milhao_af1 = vela0 + vela1 + vela2 + vela3 + vela4
      milhao_af2 = vela5 + vela6 + vela7 + vela8 + vela9   
      milhao_af3 = vela10 + vela11 + vela12 + vela13 + vela14
      
      torres_af1 = vela0
      torres_af2 = vela5
      torres_af3 = vela10
      
      padrao23_af1 = vela5
      padrao23_af2 = vela10
      padrao23_af3 = vela15
      
      melhor_af1 =vela1 + vela2 + vela3
      melhor_af2 =vela6 + vela7 + vela8  
      melhor_af3 =vela11 + vela12 + vela13
      
      padrao3x1_af1 = vela0 + vela1 + vela2
      padrao3x1_af2 = vela5 + vela6 + vela7  
      padrao3x1_af3 = vela10 + vela11 + vela12
              
      after_mhi_3 = "stop", 
      after_mhi2_3 = "stop"
      after_mhi3_3 = "stop"
      after_mhimai_3 = "stop"
      after_mhi2mai_3 = "stop"
      after_mhi3mai_3 = "stop"
      after_milhaomin_3 = "stop", 
      after_milhaomax_3 = "stop"
      after_torres_3 = "stop"
      after_padrao23_3 = "stop"
      after_melhor_3 = "stop"
      after_padrao3x1_3 = "stop"
      after_mhi_2 = "stop", 
      after_mhi2_2 = "stop"
      after_mhi3_2 = "stop"
      after_mhimai_2 = "stop"
      after_mhi2mai_2 = "stop"
      after_mhi3mai_2 = "stop"
      after_milhaomin_2 = "stop", 
      after_milhaomax_2 = "stop"
      after_torres_2 = "stop"
      after_padrao23_2 = "stop"
      after_melhor_2 = "stop"
      after_padrao3x1_2 = "stop"
      after_mhi = "stop", 
      after_mhi2 = "stop"
      after_mhi3 = "stop"
      after_mhimai = "stop"
      after_mhi2mai = "stop"
      after_mhi3mai = "stop"
      after_milhaomin = "stop", 
      after_milhaomax = "stop"
      after_torres = "stop"
      after_padrao23 = "stop"
      after_melhor = "stop"
      after_padrao3x1 = "stop"
      
      mhi_enter = "stop"
      mhi2_enter = "stop"
      mhi3_enter = "stop"
      mhimai_enter = "stop"
      mhi2mai_enter = "stop"    
      mhi3mai_enter = "stop"
      milhaomin_enter = "stop"
      milhaomax_enter = "stop"
      torres_enter = "stop"
      padrao23_enter = "stop"
      melhor_enter = "stop"    
      padrao3x1_enter = "stop" 

      if martingalaaf == 0:
       if after_loss == "3": 
        if mhi_af1 > 0 and vela5 == 1: after_mhi = "go"
        if mhi_af1 < 0 and vela5 == -1:  after_mhi = "go"
        if mhi_af1 > 0 and vela6 == 1: after_mhi2 = "go"
        if mhi_af1 < 0 and vela6 == -1:  after_mhi2 = "go"
        if mhi_af1 > 0 and vela7 == 1: after_mhi3 = "go"
        if mhi_af1 < 0 and vela7 == -1:  after_mhi3 = "go"
        if mhi_af1 > 0 and vela5 == -1: after_mhimai = "go"
        if mhi_af1 < 0 and vela5 == 1:  after_mhimai = "go"
        if mhi_af1 > 0 and vela6 == -1: after_mhi2mai = "go"
        if mhi_af1 < 0 and vela6 == 1:  after_mhi2mai = "go"
        if mhi_af1 > 0 and vela7 == -1: after_mhi3mai = "go"
        if mhi_af1 < 0 and vela7 == 1:  after_mhi3mai = "go"
        if milhao_af1 > 0 and vela5== 1: after_milhaomin = "go"
        if milhao_af1 < 0 and vela5== -1:  after_milhaomin= "go"
        if milhao_af1 > 0 and vela5== -1: after_milhaomax = "go"
        if milhao_af1 < 0 and vela5== 1:  after_milhaomax= "go"
        if torres_af1 > 0 and vela4== -1: after_torres = "go"
        if torres_af1 < 0 and vela4== 1:  after_torres = "go"
        if padrao23_af1 > 0 and vela6== -1: after_padrao23 = "go"
        if padrao23_af1 < 0 and vela6== 1:  after_padrao23 = "go"
        if padrao3x1_af1 > 0 and vela4== 1: after_padrao3x1 = "go"
        if padrao3x1_af1 < 0 and vela4== -1:  after_padrao3x1 = "go"
        if melhor_af1 > 0 and vela7== -1: after_melhor = "go"
        if melhor_af1 < 0 and vela7== 1:  after_melhor = "go"
        
       if after_loss == "3" or after_loss == "2":
        if mhi_af2 > 0 and vela10 == 1: after_mhi_2 = "go"
        if mhi_af2 < 0 and vela10 == -1:  after_mhi_2= "go"
        if mhi_af2 > 0 and vela11 == 1: after_mhi2_2 = "go"
        if mhi_af2 < 0 and vela11 == -1:  after_mhi2_2 = "go"
        if mhi_af2 > 0 and vela12 == 1: after_mhi3_2 = "go"
        if mhi_af2 < 0 and vela12 == -1:  after_mhi3_2 = "go"
        if mhi_af2 > 0 and vela10 == -1: after_mhimai_2 = "go"
        if mhi_af2 < 0 and vela10 == 1:  after_mhimai_2 = "go"
        if mhi_af2 > 0 and vela11 == -1: after_mhi2mai_2 = "go"
        if mhi_af2 < 0 and vela11 == 1:  after_mhi2mai_2 = "go"
        if mhi_af2 > 0 and vela12 == -1: after_mhi3mai_2 = "go"
        if mhi_af2 < 0 and vela12 == 1:  after_mhi3mai_2 = "go"
        if milhao_af2 > 0 and vela10== 1: after_milhaomin_2 = "go"
        if milhao_af2 < 0 and vela10== -1:  after_milhaomin_2= "go"
        if milhao_af2 > 0 and vela10== -1: after_milhaomax_2 = "go"
        if milhao_af2 < 0 and vela10== 1:  after_milhaomax_2= "go"
        if torres_af2 > 0 and vela9== -1: after_torres_2 = "go"
        if torres_af2 < 0 and vela9== 1:  after_torres_2 = "go"
        if padrao23_af2 > 0 and vela11== -1: after_padrao23_2 = "go"
        if padrao23_af2 < 0 and vela11== 1:  after_padrao23_2 = "go"
        if padrao3x1_af2 > 0 and vela9== 1: after_padrao3x1_2 = "go"
        if padrao3x1_af2 < 0 and vela9== -1:  after_padrao3x1_2 = "go"
        if melhor_af2 > 0 and vela12== -1: after_melhor_2 = "go"
        if melhor_af2 < 0 and vela12== 1:  after_melhor_2 = "go"
      
       if after_loss == "3" or after_loss == "2" or after_loss == "1": 
       
        if mhi_af3 > 0 and vela15 == 1: after_mhi_3 = "go"
        if mhi_af3 < 0 and vela15 == -1:  after_mhi_3= "go"
        if mhi_af3 > 0 and vela16 == 1: after_mhi2_3 = "go"
        if mhi_af3 < 0 and vela16 == -1:  after_mhi2_3 = "go"
        if mhi_af3 > 0 and vela17 == 1: after_mhi3_3 = "go"
        if mhi_af3 < 0 and vela17 == -1:  after_mhi3_3 = "go"
        if mhi_af3 > 0 and vela15 == -1: after_mhimai_3 = "go"
        if mhi_af3 < 0 and vela15 == 1:  after_mhimai_3 = "go"
        if mhi_af3 > 0 and vela16 == -1: after_mhi2mai_3 = "go"
        if mhi_af3 < 0 and vela16 == 1:  after_mhi2mai_3 = "go"
        if mhi_af3 > 0 and vela17 == -1: after_mhi3mai_3 = "go"
        if mhi_af3 < 0 and vela17 == 1:  after_mhi3mai_3 = "go"
        if milhao_af3 > 0 and vela15== 1: after_milhaomin_3 = "go"
        if milhao_af3 < 0 and vela15== -1:  after_milhaomin_3= "go"
        if milhao_af3 > 0 and vela15== -1: after_milhaomax_3 = "go"
        if milhao_af3 < 0 and vela15== 1:  after_milhaomax_3= "go"
        if torres_af3 > 0 and vela14== -1: after_torres_3 = "go"
        if torres_af3 < 0 and vela14== 1:  after_torres_3 = "go"
        if padrao23_af3 > 0 and vela16== -1: after_padrao23_3 = "go"
        if padrao23_af3 < 0 and vela16== 1:  after_padrao23_3 = "go"
        if padrao3x1_af3 > 0 and vela14== 1: after_padrao3x1_3 = "go"
        if padrao3x1_af3 < 0 and vela14== -1:  after_padrao3x1_3 = "go"
        if melhor_af3 > 0 and vela17== -1: after_melhor_3 = "go"
        if melhor_af3 < 0 and vela17== 1:  after_melhor_3 = "go"
        
              
      if martingalaaf == 1:        
       if after_loss == "3": 
        if mhi_af1 > 0 and vela5 + vela6 == 2: after_mhi = "go"
        if mhi_af1 < 0 and vela5 + vela6  == -2:  after_mhi = "go"
        if mhi_af1 > 0 and vela6 + vela7== 2: after_mhi2 = "go"
        if mhi_af1 < 0 and vela6 + vela7== -2:  after_mhi2 = "go"
        if mhi_af1 > 0 and vela7 + vela8 == 2: after_mhi3 = "go"
        if mhi_af1 < 0 and vela7 + vela8 == -2:  after_mhi3 = "go"
        if mhi_af1 > 0 and vela5 + vela6== -2: after_mhimai = "go"
        if mhi_af1 < 0 and vela5 + vela6== 2:  after_mhimai = "go"
        if mhi_af1 > 0 and vela6 + vela7== -2: after_mhi2mai = "go"
        if mhi_af1 < 0 and vela6 + vela7== 2:  after_mhi2mai = "go"
        if mhi_af1 > 0 and vela7 + vela8== -2: after_mhi3mai = "go"
        if mhi_af1 < 0 and vela7 + vela8== 2:  after_mhi3mai = "go"
        if milhao_af1 > 0 and vela5 + vela6== 2: after_milhaomin = "go"
        if milhao_af1 < 0 and vela5 + vela6== -2:  after_milhaomin= "go"
        if milhao_af1 > 0 and vela5 + vela6== -2: after_milhaomax = "go"
        if milhao_af1 < 0 and vela5 + vela6== 2:  after_milhaomax= "go"
        if torres_af1 > 0 and vela4 + vela5== -2: after_torres = "go"
        if torres_af1 < 0 and vela4 + vela5== 2:  after_torres = "go"
        if padrao23_af1 > 0 and vela6 + vela7== -2: after_padrao23 = "go"
        if padrao23_af1 < 0 and vela6 + vela7== 2:  after_padrao23 = "go"
        if padrao3x1_af1 > 0 and vela4 + vela5== 2: after_padrao3x1 = "go"
        if padrao3x1_af1 < 0 and vela4 + vela5== -2:  after_padrao3x1 = "go"
        if melhor_af1 > 0 and vela7 + vela8== -2: after_melhor = "go"
        if melhor_af1 < 0 and vela7 + vela8== 2:  after_melhor = "go"
    
       if after_loss == "3" or after_loss == "2":
        if mhi_af2 > 0 and vela10 + vela11 == 2: after_mhi_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11== -2:  after_mhi_2= "go"
        if mhi_af2 > 0 and vela11 + vela12== 2: after_mhi2_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 == -2:  after_mhi2_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 == 2: after_mhi3_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13== -2:  after_mhi3_2 = "go"
        if mhi_af2 > 0 and vela10 + vela11== -2: after_mhimai_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11== 2:  after_mhimai_2 = "go"
        if mhi_af2 > 0 and vela11 + vela12== -2: after_mhi2mai_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12== 2:  after_mhi2mai_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13== -2: after_mhi3mai_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13== 2:  after_mhi3mai_2 = "go"
        if milhao_af2 > 0 and vela10 + vela11== 2: after_milhaomin_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11== -2:  after_milhaomin_2= "go"
        if milhao_af2 > 0 and vela10 + vela11== -2: after_milhaomax_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11== 2:  after_milhaomax_2= "go"
        if torres_af2 > 0 and vela9 + vela10== -2: after_torres_2 = "go"
        if torres_af2 < 0 and vela9 + vela10== 2:  after_torres_2 = "go"
        if padrao23_af2 > 0 and vela11 + vela12== -2: after_padrao23_2 = "go"
        if padrao23_af2 < 0 and vela11 + vela12== 2:  after_padrao23_2 = "go"
        if padrao3x1_af2 > 0 and vela9 + vela10== 2: after_padrao3x1_2 = "go"
        if padrao3x1_af2 < 0 and vela9 + vela10== -2:  after_padrao3x1_2 = "go"
        if melhor_af2 > 0 and vela12 + vela13== -2: after_melhor_2 = "go"
        if melhor_af2 < 0 and vela12 + vela13== 2:  after_melhor_2 = "go" 
      
       if after_loss == "3" or after_loss == "2" or after_loss == "1":  
        if mhi_af3 > 0 and vela15 + vela16== 2: after_mhi_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16== -2:  after_mhi_3= "go"
        if mhi_af3 > 0 and vela16 + vela17== 2: after_mhi2_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 == -2:  after_mhi2_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18 == 2: after_mhi3_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18== -2:  after_mhi3_3 = "go"
        if mhi_af3 > 0 and vela15 + vela16== -2: after_mhimai_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16== 2:  after_mhimai_3 = "go"
        if mhi_af3 > 0 and vela16 + vela17== -2: after_mhi2mai_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17== 2:  after_mhi2mai_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18== -2: after_mhi3mai_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18== 2:  after_mhi3mai_3 = "go"
        if milhao_af3 > 0 and vela15 + vela16== 2: after_milhaomin_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16== -2:  after_milhaomin_3= "go"
        if milhao_af3 > 0 and vela15 + vela16== -2: after_milhaomax_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16== 2:  after_milhaomax_3= "go"
        if torres_af3 > 0 and vela14 + vela15== -2: after_torres_3 = "go"
        if torres_af3 < 0 and vela14 + vela15== 2:  after_torres_3 = "go"
        if padrao23_af3 > 0 and vela16 + vela17== -2: after_padrao23_3 = "go"
        if padrao23_af3 < 0 and vela16 + vela17== 2:  after_padrao23_3 = "go"
        if padrao3x1_af3 > 0 and vela14 + vela15== 2: after_padrao3x1_3 = "go"
        if padrao3x1_af3 < 0 and vela14 + vela15== -2:  after_padrao3x1_3 = "go"
        if melhor_af3 > 0 and vela17 + vela18== -2: after_melhor_3 = "go"
        if melhor_af3 < 0 and vela17 + vela18== 2:  after_melhor_3 = "go"
          
      if martingalaaf == 2:
       if after_loss == "3": 
        if mhi_af1 > 0 and vela5 + vela6 + vela7 == 3: after_mhi = "go"
        if mhi_af1 < 0 and vela5 + vela6 + vela7 == -3:  after_mhi = "go"
        if mhi_af1 > 0 and vela6 + vela7 + vela8== 3: after_mhi2 = "go"
        if mhi_af1 < 0 and vela6 + vela7 + vela8== -3:  after_mhi2 = "go"
        if mhi_af1 > 0 and vela7 + vela8 + vela9== 3: after_mhi3 = "go"
        if mhi_af1 < 0 and vela7 + vela8 + vela9== -3:  after_mhi3 = "go"
        if mhi_af1 > 0 and vela5 + vela6 + vela7== -3: after_mhimai = "go"
        if mhi_af1 < 0 and vela5 + vela6 + vela7== 3:  after_mhimai = "go"
        if mhi_af1 > 0 and vela6 + vela7 + vela8== -3: after_mhi2mai = "go"
        if mhi_af1 < 0 and vela6 + vela7 + vela8== 3:  after_mhi2mai = "go"
        if mhi_af1 > 0 and vela7 + vela8 + vela9== -3: after_mhi3mai = "go"
        if mhi_af1 < 0 and vela7 + vela8 + vela9== 3:  after_mhi3mai = "go"
        if milhao_af1 > 0 and vela5 + vela6 + vela7== 3: after_milhaomin = "go"
        if milhao_af1 < 0 and vela5 + vela6 + vela7== -3:  after_milhaomin= "go"
        if milhao_af1 > 0 and vela5 + vela6 + vela7== -3: after_milhaomax = "go"
        if milhao_af1 < 0 and vela5 + vela6 + vela7== 3:  after_milhaomax= "go"
        if torres_af1 > 0 and vela4 + vela5 + vela6== -3: after_torres = "go"
        if torres_af1 < 0 and vela4 + vela5 + vela6 == 3:  after_torres = "go"
        if padrao23_af1 > 0 and vela6 + vela7 + vela8== -3: after_padrao23 = "go"
        if padrao23_af1 < 0 and vela6 + vela7 + vela8== 3:  after_padrao23 = "go"
        if padrao3x1_af1 > 0 and vela4 + vela5 + vela6== 3: after_padrao3x1 = "go"
        if padrao3x1_af1 < 0 and vela4 + vela5 + vela6== -3:  after_padrao3x1 = "go"
        if melhor_af1 > 0 and vela7 + vela8 + vela9== -3: after_melhor = "go"
        if melhor_af1 < 0 and vela7 + vela8 + vela9== 3:  after_melhor = "go"
        
       if after_loss == "3" or after_loss == "2":
        if mhi_af2 > 0 and vela10 + vela11 + vela12 == 3: after_mhi_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11 + vela12== -3:  after_mhi_2= "go"
        if mhi_af2 > 0 and vela11 + vela12 + vela13== 3: after_mhi2_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 + vela13 == -3:  after_mhi2_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 + vela14 == 3: after_mhi3_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13 + vela14== -3:  after_mhi3_2 = "go"
        if mhi_af2 > 0 and vela10 + vela11 + vela12== -3: after_mhimai_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11 + vela12== 3:  after_mhimai_2 = "go"
        if mhi_af2 > 0 and vela11 + vela12 + vela13== -3: after_mhi2mai_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 + vela13== 3:  after_mhi2mai_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 + vela14== -3: after_mhi3mai_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13 + vela14== 3:  after_mhi3mai_2 = "go"
        if milhao_af2 > 0 and vela10 + vela11 + vela12== 3: after_milhaomin_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11 + vela12== -3:  after_milhaomin_2= "go"
        if milhao_af2 > 0 and vela10 + vela11 + vela12== -3: after_milhaomax_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11 + vela12== 3:  after_milhaomax_2= "go"
        if torres_af2 > 0 and vela9 + vela10 + vela11== -3: after_torres_2 = "go"
        if torres_af2 < 0 and vela9 + vela10 + vela11== 3:  after_torres_2 = "go"
        if padrao23_af2 > 0 and vela11 + vela12 + vela13== -3: after_padrao23_2 = "go"
        if padrao23_af2 < 0 and vela11 + vela12 + vela13== 3:  after_padrao23_2 = "go"
        if padrao3x1_af2 > 0 and vela9 + vela10 + vela11== 3: after_padrao3x1_2 = "go"
        if padrao3x1_af2 < 0 and vela9 + vela10 + vela11== -3:  after_padrao3x1_2 = "go"
        if melhor_af2 > 0 and vela12 + vela13 + vela14== -3: after_melhor_2 = "go"
        if melhor_af2 < 0 and vela12 + vela13 + vela14== 3:  after_melhor_2 = "go" 
       
       if after_loss == "3" or after_loss == "2" or after_loss == "1": 
       
        if mhi_af3 > 0 and vela15 + vela16 + vela17== 3: after_mhi_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16 + vela17== -3:  after_mhi_3= "go"
        if mhi_af3 > 0 and vela16 + vela17 + vela18== 3: after_mhi2_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 + vela18== -3:  after_mhi2_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18 + vela19== 3: after_mhi3_3 = "go"       
        if mhi_af3 < 0 and vela17 + vela18 + vela19== -3:  after_mhi3_3 = "go"
        if mhi_af3 > 0 and vela15 + vela16 + vela17== -3: after_mhimai_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16 + vela17== 3:  after_mhimai_3 = "go"
        if mhi_af3 > 0 and vela16 + vela17 + vela18== -3: after_mhi2mai_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 + vela18== 3:  after_mhi2mai_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18 + vela19== -3: after_mhi3mai_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18 + vela19== 3:  after_mhi3mai_3 = "go"
        if milhao_af3 > 0 and vela15 + vela16 + vela17== 3: after_milhaomin_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16 + vela17== -3:  after_milhaomin_3= "go"
        if milhao_af3 > 0 and vela15 + vela16 + vela17== -3: after_milhaomax_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16 + vela17== 3:  after_milhaomax_3= "go"
        if torres_af3 > 0 and vela14 + vela15 + vela16== -3: after_torres_3 = "go"
        if torres_af3 < 0 and vela14 + vela15 + vela16== 3:  after_torres_3 = "go"
        if padrao23_af3 > 0 and vela16 + vela17 + vela18== -3: after_padrao23_3 = "go"
        if padrao23_af3 < 0 and vela16 + vela17 + vela18== 3:  after_padrao23_3 = "go"
        if padrao3x1_af3 > 0 and vela14 + vela15 + vela16== 3: after_padrao3x1_3 = "go"
        if padrao3x1_af3 < 0 and vela14 + vela15 + vela16== -3:  after_padrao3x1_3 = "go"
        if melhor_af3 > 0 and vela17 + vela18 + vela19== -3: after_melhor_3 = "go"
        if melhor_af3 < 0 and vela17 + vela18 + vela19== 3:  after_melhor_3 = "go"
        
      if martingalaaf == 3:
       if after_loss == "3": 
        if mhi_af1 > 0 and vela5 + vela6 + vela7 + vela8 == 4: after_mhi = "go"
        if mhi_af1 < 0 and vela5 + vela6 + vela7 + vela8 == -4:  after_mhi = "go"
        if mhi_af1 > 0 and vela6 + vela7 + vela8 + vela9== 4: after_mhi2 = "go"
        if mhi_af1 < 0 and vela6 + vela7 + vela8 + vela9== -4:  after_mhi2 = "go"
        if mhi_af1 > 0 and vela7 + vela8 + vela9 + vela10== 4: after_mhi3 = "go"
        if mhi_af1 < 0 and vela7 + vela8 + vela9 + vela10== -4:  after_mhi3 = "go"
        if mhi_af1 > 0 and vela5 + vela6 + vela7 + vela8== -4: after_mhimai = "go"
        if mhi_af1 < 0 and vela5 + vela6 + vela7 + vela8== 4:  after_mhimai = "go"
        if mhi_af1 > 0 and vela6 + vela7 + vela8 + vela9== -4: after_mhi2mai = "go"
        if mhi_af1 < 0 and vela6 + vela7 + vela8 + vela9== 4:  after_mhi2mai = "go"
        if mhi_af1 > 0 and vela7 + vela8 + vela9 + vela10== -4: after_mhi3mai = "go"
        if mhi_af1 < 0 and vela7 + vela8 + vela9 + vela10== 4:  after_mhi3mai = "go"
        if milhao_af1 > 0 and vela5 + vela6 + vela7 + vela8== 4: after_milhaomin = "go"
        if milhao_af1 < 0 and vela5 + vela6 + vela7 + vela8== -4:  after_milhaomin= "go"
        if milhao_af1 > 0 and vela5 + vela6 + vela7 + vela8== -4: after_milhaomax = "go"
        if milhao_af1 < 0 and vela5 + vela6 + vela7 + vela8== 4:  after_milhaomax = "go"
        if torres_af1 > 0 and vela4 + vela5 + vela6 + vela7== -4: after_torres = "go"
        if torres_af1 < 0 and vela4 + vela5 + vela6 + vela7 == 4:  after_torres = "go"
        if padrao23_af1 > 0 and vela6 + vela7 + vela8 + vela9== -4: after_padrao23 = "go"
        if padrao23_af1 < 0 and vela6 + vela7 + vela8 + vela9== 4:  after_padrao23 = "go"
        if padrao3x1_af1 > 0 and vela4 + vela5 + vela6 + vela7== 4: after_padrao3x1 = "go"
        if padrao3x1_af1 < 0 and vela4 + vela5 + vela6 + vela7== -4:  after_padrao3x1 = "go"
        if melhor_af1 > 0 and vela7 + vela8 + vela9 + vela10== -4: after_melhor = "go"
        if melhor_af1 < 0 and vela7 + vela8 + vela9 + vela10== 4:  after_melhor = "go" 
        
       if after_loss == "3" or after_loss == "2":
        if mhi_af2 > 0 and vela10 + vela11 + vela12 + vela13 == 4: after_mhi_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11 + vela12 + vela13== -4:  after_mhi_2= "go"
        if mhi_af2 > 0 and vela11 + vela12 + vela13 + vela14== 4: after_mhi2_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 + vela13 + vela14 == -4:  after_mhi2_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 + vela14 + vela15 == 4: after_mhi3_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13 + vela14 + vela15== -4:  after_mhi3_2 = "go"
        if mhi_af2 > 0 and vela10 + vela11 + vela12 + vela13== -4: after_mhimai_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11 + vela12 + vela13== 4:  after_mhimai_2 = "go"
        if mhi_af2 > 0 and vela11 + vela12 + vela13 + vela14== -4: after_mhi2mai_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 + vela13 + vela14== 4:  after_mhi2mai_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 + vela14 + vela15== -4: after_mhi3mai_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13 + vela14 + vela15== 4:  after_mhi3mai_2 = "go" 
        if milhao_af2 > 0 and vela10 + vela11 + vela12 + vela13== 4: after_milhaomin_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11 + vela12 + vela13== -4:  after_milhaomin_2= "go"
        if milhao_af2 > 0 and vela10 + vela11 + vela12 + vela13== -4: after_milhaomax_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11 + vela12 + vela13== 4:  after_milhaomax_2= "go"
        if torres_af2 > 0 and vela9 + vela10 + vela11 + vela12== -4: after_torres_2 = "go"
        if torres_af2 < 0 and vela9 + vela10 + vela11 + vela12 == 4:  after_torres_2 = "go"
        if padrao23_af2 > 0 and vela11 + vela12 + vela13 + vela14== -4: after_padrao23_2 = "go"
        if padrao23_af2 < 0 and vela11 + vela12 + vela13 + vela14== 4:  after_padrao23_2 = "go"
        if padrao3x1_af2 > 0 and vela9 + vela10 + vela11 + vela12== 4: after_padrao3x1_2 = "go"
        if padrao3x1_af2 < 0 and vela9 + vela10 + vela11 + vela12== -4:  after_padrao3x1_2 = "go"
        if melhor_af2 > 0 and vela12 + vela13 + vela14 + vela15== -4: after_melhor_2 = "go"
        if melhor_af2 < 0 and vela12 + vela13 + vela14 + vela15== 4:  after_melhor_2 = "go" 
       
       if after_loss == "3" or after_loss == "2" or after_loss == "1": 
       
        if mhi_af3 > 0 and vela15 + vela16 + vela17 + vela18== 4: after_mhi_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16 + vela17 + vela18== -4:  after_mhi_3= "go"
        if mhi_af3 > 0 and vela16 + vela17 + vela18 + vela19== 4: after_mhi2_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 + vela18 + vela19== -4:  after_mhi2_3 = "go"
        if mhi_af3 > 0 and vela15 + vela16 + vela17 + vela18== -4: after_mhimai_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16 + vela17 + vela18== 4:  after_mhimai_3 = "go"
        if mhi_af3 > 0 and vela16 + vela17 + vela18 + vela19== -4: after_mhi2mai_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 + vela18 + vela19== 4:  after_mhi2mai_3 = "go"
        if milhao_af3 > 0 and vela15 + vela16 + vela17 + vela18== 4: after_milhaomin_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16 + vela17 + vela18== -4:  after_milhaomin_3= "go"
        if milhao_af3 > 0 and vela15 + vela16 + vela17 + vela18== -4: after_milhaomax_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16 + vela17 + vela18== 4:  after_milhaomax_3= "go"
        if torres_af3 > 0 and vela14 + vela15 + vela16 + vela17== -4: after_torres_3 = "go"
        if torres_af3 < 0 and vela14 + vela15 + vela16 + vela17 == 4:  after_torres_3 = "go"
        if padrao23_af3 > 0 and vela16 + vela17 + vela18 + vela19== -4: after_padrao23_3 = "go"
        if padrao23_af3 < 0 and vela16 + vela17 + vela18 + vela19== 4:  after_padrao23_3 = "go"
        if padrao3x1_af3 > 0 and vela14 + vela15 + vela16 + vela17== 4: after_padrao3x1_3 = "go"
        if padrao3x1_af3 < 0 and vela14 + vela15 + vela16 + vela17== -4:  after_padrao3x1_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18 + vela19 + vela20== -4: after_mhi3mai_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18 + vela19 + vela20== 4:  after_mhi3mai_3 = "go" 
        if mhi_af3 > 0 and vela17 + vela18 + vela19 + vela20== 4: after_mhi3_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18 + vela19 + vela20== -4:  after_mhi3_3 = "go"
        if melhor_af3 > 0 and vela17 + vela18 + vela19 + vela20== -4: after_melhor_3 = "go"
        if melhor_af3 < 0 and vela17 + vela18 + vela19 + vela20== 4:  after_melhor_3 = "go" 
        
      if martingalaaf == 4:
       if after_loss == "3": 
        if mhi_af1 > 0 and vela5 + vela6 + vela7 + vela8 + vela9 == 5: after_mhi = "go"
        if mhi_af1 < 0 and vela5 + vela6 + vela7 + vela8 + vela9== -5:  after_mhi = "go"
        if mhi_af1 > 0 and vela6 + vela7 + vela8 + vela9 + vela10== 5: after_mhi2 = "go"
        if mhi_af1 < 0 and vela6 + vela7 + vela8 + vela9 + vela10== -5:  after_mhi2 = "go"
        if mhi_af1 > 0 and vela7 + vela8 + vela9 + vela10 + vela11== 5: after_mhi3 = "go"
        if mhi_af1 < 0 and vela7 + vela8 + vela9 + vela10 + vela11== -5:  after_mhi3 = "go"
        if mhi_af1 > 0 and vela5 + vela6 + vela7 + vela8 + vela9== -5: after_mhimai = "go"
        if mhi_af1 < 0 and vela5 + vela6 + vela7 + vela8 + vela9== 5:  after_mhimai = "go"
        if mhi_af1 > 0 and vela6 + vela7 + vela8 + vela9 + vela10== -5: after_mhi2mai = "go"
        if mhi_af1 < 0 and vela6 + vela7 + vela8 + vela9 + vela10== 5:  after_mhi2mai = "go"
        if mhi_af1 > 0 and vela7 + vela8 + vela9 + vela10 + vela11== -5: after_mhi3mai = "go"
        if mhi_af1 < 0 and vela7 + vela8 + vela9 + vela10 + vela11== 5:  after_mhi3mai = "go"
        if milhao_af1 > 0 and vela10 + vela11 + vela12 + vela13 + vela14== 5: after_milhaomin = "go"
        if milhao_af1 < 0 and vela10 + vela11 + vela12 + vela13 + vela14== -5:  after_milhaomin= "go"
        if milhao_af1 > 0 and vela10 + vela11 + vela12 + vela13 + vela14== -5: after_milhaomax = "go"
        if milhao_af1 < 0 and vela10 + vela11 + vela12 + vela13 + vela14== +5:  after_milhaomax= "go"
        if torres_af1 > 0 and vela9 + vela10 + vela11 + vela12 + vela13== -5: after_torres = "go"
        if torres_af1 < 0 and vela9 + vela10 + vela11 + vela12 + vela13 == 5:  after_torres = "go"
        if padrao23_af1 > 0 and vela11 + vela12 + vela13 + vela14 + vela15== -5: after_padrao23 = "go"
        if padrao23_af1 < 0 and vela11 + vela12 + vela13 + vela14 + vela15== 5:  after_padrao23 = "go"
        if melhor_af1 > 0 and vela12 + vela13 + vela14 + vela15 + vela16== -5: after_melhor = "go"
        if melhor_af1 < 0 and vela12 + vela13 + vela14 + vela15 + vela16== 5:  after_melhor = "go"
        if padrao3x1_af1 > 0 and vela9 + vela10 + vela11 + vela12 + vela13== 5: after_padrao3x1 = "go"
        if padrao3x1_af1 < 0 and vela9 + vela10 + vela11 + vela12 + vela13== -5:  after_padrao3x1 = "go"
        
       if after_loss == "3" or after_loss == "2":
        if mhi_af2 > 0 and vela10 + vela11 + vela12 + vela13 + vela14 == 5: after_mhi_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11 + vela12 + vela13 + vela14== -5:  after_mhi_2= "go"
        if mhi_af2 > 0 and vela11 + vela12 + vela13 + vela14 + vela15== 5: after_mhi2_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 + vela13 + vela14 + vela15 == -5:  after_mhi2_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 + vela14 + vela15 + vela16 == 5: after_mhi3_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13 + vela14 + vela15 + vela16== -5:  after_mhi3_2 = "go"
        if mhi_af2 > 0 and vela10 + vela11 + vela12 + vela13 + vela14== -5: after_mhimai_2 = "go"
        if mhi_af2 < 0 and vela10 + vela11 + vela12 + vela13 + vela14== 5:  after_mhimai_2 = "go"
        if mhi_af2 > 0 and vela11 + vela12 + vela13 + vela14 + vela15== -5: after_mhi2mai_2 = "go"
        if mhi_af2 < 0 and vela11 + vela12 + vela13 + vela14 + vela15== 5:  after_mhi2mai_2 = "go"
        if mhi_af2 > 0 and vela12 + vela13 + vela14 + vela15 + vela16== -5: after_mhi3mai_2 = "go"
        if mhi_af2 < 0 and vela12 + vela13 + vela14 + vela15 + vela16== 5:  after_mhi3mai_2 = "go" 
        if milhao_af2 > 0 and vela10 + vela11 + vela12 + vela13 + vela14== 5: after_milhaomin_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11 + vela12 + vela13 + vela14== -5:  after_milhaomin_2= "go"
        if milhao_af2 > 0 and vela10 + vela11 + vela12 + vela13 + vela14== -5: after_milhaomax_2 = "go"
        if milhao_af2 < 0 and vela10 + vela11 + vela12 + vela13 + vela14== +5:  after_milhaomax_2= "go"
        if torres_af2 > 0 and vela9 + vela10 + vela11 + vela12 + vela13== -5: after_torres_2 = "go"
        if torres_af2 < 0 and vela9 + vela10 + vela11 + vela12 + vela13 == 5:  after_torres_2 = "go"
        if padrao23_af2 > 0 and vela11 + vela12 + vela13 + vela14 + vela15== -5: after_padrao23_2 = "go"
        if padrao23_af2 < 0 and vela11 + vela12 + vela13 + vela14 + vela15== 5:  after_padrao23_2 = "go"
        if melhor_af2 > 0 and vela12 + vela13 + vela14 + vela15 + vela16== -5: after_melhor_2 = "go"
        if melhor_af2 < 0 and vela12 + vela13 + vela14 + vela15 + vela16== 5:  after_melhor_2 = "go"
        if padrao3x1_af2 > 0 and vela9 + vela10 + vela11 + vela12 + vela13== 5: after_padrao3x1_2 = "go"
        if padrao3x1_af2 < 0 and vela9 + vela10 + vela11 + vela12 + vela13== -5:  after_padrao3x1_2 = "go"
       
       if after_loss == "3" or after_loss == "2" or after_loss == "1": 
       
        if mhi_af3 > 0 and vela15 + vela16 + vela17 + vela18 + vela19== 5: after_mhi_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16 + vela17 + vela18 + vela19== -5:  after_mhi_3= "go"
        if mhi_af3 > 0 and vela15 + vela16 + vela17 + vela18 + vela19== -5: after_mhimai_3 = "go"
        if mhi_af3 < 0 and vela15 + vela16 + vela17 + vela18 + vela19== 5:  after_mhimai_3 = "go"
        if milhao_af3 > 0 and vela15 + vela16 + vela17 + vela18 + vela19== 5: after_milhaomin_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16 + vela17 + vela18 + vela19== -5:  after_milhaomin_3= "go"
        if milhao_af3 > 0 and vela15 + vela16 + vela17 + vela18 + vela19== -5: after_milhaomax_3 = "go"
        if milhao_af3 < 0 and vela15 + vela16 + vela17 + vela18 + vela19== 5:  after_milhaomax_3= "go"
        if torres_af3 > 0 and vela14 + vela15 + vela16 + vela17 + vela18== -5: after_torres_3 = "go"
        if torres_af3 < 0 and vela14 + vela15 + vela16 + vela17 + vela18== 5:  after_torres_3 = "go"
        if padrao3x1_af3 > 0 and vela14 + vela15 + vela16 + vela17 + vela18== 5: after_padrao3x1_3 = "go"
        if padrao3x1_af3 < 0 and vela14 + vela15 + vela16 + vela17 + vela18== -5:  after_padrao3x1_3 = "go"
        if mhi_af3 > 0 and vela16 + vela17 + vela18 + vela19 + vela20== 5: after_mhi2_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 + vela18 + vela19 + vela20== -5:  after_mhi2_3 = "go"
        if mhi_af3 > 0 and vela16 + vela17 + vela18 + vela19 + vela20== -5: after_mhi2mai_3 = "go"
        if mhi_af3 < 0 and vela16 + vela17 + vela18 + vela19 + vela20== 5:  after_mhi2mai_3 = "go"
        if padrao23_af3 > 0 and vela16 + vela17 + vela18 + vela19 + vela20== -5: after_padrao23_3 = "go"
        if padrao23_af3 < 0 and vela16 + vela17 + vela18 + vela19 + vela20== 5:  after_padrao23_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18 + vela19 + vela20 + vela21== 5: after_mhi3_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18 + vela19 + vela20 + vela21== -5:  after_mhi3_3 = "go"
        if mhi_af3 > 0 and vela17 + vela18 + vela19 + vela20 + vela21== -5: after_mhi3mai_3 = "go"
        if mhi_af3 < 0 and vela17 + vela18 + vela19 + vela20 + vela21== 5:  after_mhi3mai_3 = "go" 
        if melhor_af3 > 0 and vela17 + vela18 + vela19 + vela20 + vela21== -5: after_melhor_3 = "go"
        if melhor_af3 < 0 and vela17 + vela18 + vela19 + vela20 + vela21== 5:  after_melhor_3 = "go" 
      
  
      if after_loss =="1":
        if after_mhi_3 == "go": mhi_enter = "go"
        if after_mhi2_3 == "go": mhi2_enter = "go"
        if after_mhi3_3 == "go": mhi3_enter = "go"
        if after_mhimai_3 == "go": mhimai_enter = "go"
        if after_mhi2mai_3 == "go": mhi2mai_enter = "go"    
        if after_mhi3mai_3 == "go": mhi3mai_enter = "go"
        if after_milhaomin_3 == "go": milhaomin_enter = "go"
        if after_milhaomax_3 == "go": milhaomax_enter = "go"
        if after_torres_3 == "go": torres_enter = "go"
        if after_padrao23_3 == "go": padrao23_enter = "go"
        if after_melhor_3 == "go": melhor_enter = "go"    
        if after_padrao3x1_3 == "go": padrao3x1_enter = "go"
        
      if after_loss =="2":
        if after_mhi_3 == "go" and after_mhi_2 == "go": mhi_enter = "go"
        if after_mhi2_3 == "go" and after_mhi2_2 == "go": mhi2_enter = "go"
        if after_mhi3_3 == "go" and after_mhi3_2 == "go": mhi3_enter = "go"
        if after_mhimai_3 == "go" and after_mhimai_2 == "go": mhimai_enter = "go"
        if after_mhi2mai_3 == "go" and after_mhi2mai_2 == "go": mhi2mai_enter = "go"    
        if after_mhi3mai_3 == "go" and after_mhi3mai_2 == "go": mhi3mai_enter = "go"
        if after_milhaomin_3 == "go" and after_milhaomin_2 == "go": milhaomin_enter = "go"
        if after_milhaomax_3 == "go" and after_milhaomax_2 == "go": milhaomax_enter = "go"
        if after_torres_3 == "go" and after_torres_2 == "go": torres_enter = "go"
        if after_padrao23_3 == "go" and after_padrao23_2 == "go": padrao23_enter = "go"
        if after_melhor_3 == "go" and after_melhor_2 == "go" : melhor_enter = "go"    
        if after_padrao3x1_3 == "go" and after_padrao3x1_2 == "go": padrao3x1_enter = "go"
        
      if after_loss =="3":
        if after_mhi_3 == "go" and after_mhi_2 == "go" and after_mhi : mhi_enter = "go"
        if after_mhi2_3 == "go" and after_mhi2_2 == "go" and after_mhi2 : mhi2_enter = "go"
        if after_mhi3_3 == "go" and after_mhi3_2 == "go" and after_mhi3 : mhi3_enter = "go"
        if after_mhimai_3 == "go" and after_mhimai_2 == "go" and after_mhimai : mhimai_enter = "go"
        if after_mhi2mai_3 == "go" and after_mhi2mai_2 == "go" and after_mhi2mai : mhi2mai_enter = "go"    
        if after_mhi3mai_3 == "go" and after_mhi3mai_2 == "go" and after_mhi3mai : mhi3mai_enter = "go" 
        if after_milhaomin_3 == "go" and after_milhaomin_2 == "go" and after_milhaomin : milhaomin_enter = "go"
        if after_milhaomax_3 == "go" and after_milhaomax_2 == "go" and after_milhaomax : milhaomax_enter = "go"
        if after_torres_3 == "go" and after_torres_2 == "go" and after_torres : torres_enter = "go"
        if after_padrao23_3 == "go" and after_padrao23_2 == "go" and after_padrao23 : padrao23_enter = "go"
        if after_melhor_3 == "go" and after_melhor_2 == "go" and after_melhor: melhor_enter = "go"    
        if after_padrao3x1_3 == "go" and after_padrao3x1_2 == "go" and after_padrao3x1: padrao3x1_enter = "go"         
         
      if after_loss =="1":
        if after_mhi_3 == "go": mhi_enter = "go"
        if after_mhi2_3 == "go": mhi2_enter = "go"
        if after_mhi3_3 == "go": mhi3_enter = "go"
        if after_mhimai_3 == "go": mhimai_enter = "go"
        if after_mhi2mai_3 == "go": mhi2mai_enter = "go"    
        if after_mhi3mai_3 == "go": mhi3mai_enter = "go"
        if after_milhaomin_3 == "go": milhaomin_enter = "go"
        if after_milhaomax_3 == "go": milhaomax_enter = "go"
        if after_torres_3 == "go": torres_enter = "go"
        if after_padrao23_3 == "go": padrao23_enter = "go"
        if after_melhor_3 == "go": melhor_enter = "go"    
        if after_padrao3x1_3 == "go": padrao3x1_enter = "go"
        
      if after_loss =="2":
        if after_mhi_3 == "go" and after_mhi_2 == "go": mhi_enter = "go"
        if after_mhi2_3 == "go" and after_mhi2_2 == "go": mhi2_enter = "go"
        if after_mhi3_3 == "go" and after_mhi3_2 == "go": mhi3_enter = "go"
        if after_mhimai_3 == "go" and after_mhimai_2 == "go": mhimai_enter = "go"
        if after_mhi2mai_3 == "go" and after_mhi2mai_2 == "go": mhi2mai_enter = "go"    
        if after_mhi3mai_3 == "go" and after_mhi3mai_2 == "go": mhi3mai_enter = "go"
        if after_milhaomin_3 == "go" and after_milhaomin_2 == "go": milhaomin_enter = "go"
        if after_milhaomax_3 == "go" and after_milhaomax_2 == "go": milhaomax_enter = "go"
        if after_torres_3 == "go" and after_torres_2 == "go": torres_enter = "go"
        if after_padrao23_3 == "go" and after_padrao23_2 == "go": padrao23_enter = "go"
        if after_melhor_3 == "go" and after_melhor_2 == "go" : melhor_enter = "go"    
        if after_padrao3x1_3 == "go" and after_padrao3x1_2 == "go": padrao3x1_enter = "go"
        
      if after_loss =="3":
        if after_mhi_3 == "go" and after_mhi_2 == "go" and after_mhi : mhi_enter = "go"
        if after_mhi2_3 == "go" and after_mhi2_2 == "go" and after_mhi2 : mhi2_enter = "go"
        if after_mhi3_3 == "go" and after_mhi3_2 == "go" and after_mhi3 : mhi3_enter = "go"
        if after_mhimai_3 == "go" and after_mhimai_2 == "go" and after_mhimai : mhimai_enter = "go"
        if after_mhi2mai_3 == "go" and after_mhi2mai_2 == "go" and after_mhi2mai : mhi2mai_enter = "go"    
        if after_mhi3mai_3 == "go" and after_mhi3mai_2 == "go" and after_mhi3mai : mhi3mai_enter = "go" 
        if after_milhaomin_3 == "go" and after_milhaomin_2 == "go" and after_milhaomin : milhaomin_enter = "go"
        if after_milhaomax_3 == "go" and after_milhaomax_2 == "go" and after_milhaomax : milhaomax_enter = "go"
        if after_torres_3 == "go" and after_torres_2 == "go" and after_torres : torres_enter = "go"
        if after_padrao23_3 == "go" and after_padrao23_2 == "go" and after_padrao23 : padrao23_enter = "go"
        if after_melhor_3 == "go" and after_melhor_2 == "go" and after_melhor: melhor_enter = "go"    
        if after_padrao3x1_3 == "go" and after_padrao3x1_2 == "go" and after_padrao3x1: padrao3x1_enter = "go" 
      
      if after_loss == "0":
        mhi_enter = "go"
        mhi2_enter = "go"
        mhi3_enter = "go"
        mhimai_enter = "go"
        mhi2mai_enter = "go"    
        mhi3mai_enter = "go"
        milhaomin_enter = "go"
        milhaomax_enter = "go"
        torres_enter = "go"
        padrao23_enter = "go"
        melhor_enter = "go"    
        padrao3x1_enter = "go"





        
      global action_mhi  
      global action_mhi2
      global action_mhi3
      global action_mhimai
      global action_mhi2mai
      global action_mhi3mai
      action_mhi = "none"
      action_mhi2 = "none"
      action_mhi3 = "none"
      action_mhimai = "none"
      action_mhi2mai = "none"
      action_mhi3mai = "none"
      action_milhaomin = "none"
      action_milhaomax = "none"
      action_torres= "none"
      action_padrao23 = "none"
      action_melhor = "none"
      action_padrao3x1 = "none"  
                
      if hora_entrar_mhi == 0 + n1 or  hora_entrar_mhi == 5 + n1:
         mhi = vela17 + vela18 + vela19 
         milhao = vela15 + vela16 + vela17 + vela18 + vela19
         if modo_entrada == 1:
            if mhi > 0: action_mhi = "put"
            if mhi < 0: action_mhi = "call"
            if mhi > 0: action_mhimai = "call"
            if mhi < 0: action_mhimai = "put"
            if milhao > 0: action_milhaomin = "put"
            if milhao < 0: action_milhaomin = "call"
            if milhao > 0: action_milhaomax = "call"
            if milhao < 0: action_milhaomax = "put" 
         if modo_entrada == 2:
            mg_1 = vela20 
            if mhi > 0 and mg_1 == 1: action_mhi = "put"
            if mhi < 0 and mg_1 == -1: action_mhi = "call"
            if mhi > 0 and mg_1 == -1: action_mhimai = "call"
            if mhi < 0 and mg_1 == 1: action_mhimai = "put"
            if milhao > 0 and mg_1 == 1: action_milhaomin = "put"
            if milhao < 0 and mg_1 == -1: action_milhaomin = "call"
            if milhao > 0 and mg_1 == -1: action_milhaomax = "call"
            if milhao < 0 and mg_1 == 1: action_milhaomax = "put"
         if modo_entrada == 3:
            mg_1 = vela20 + vela21
            if mhi > 0 and mg_1 == 2: action_mhi = "put"
            if mhi < 0 and mg_1 == -2: action_mhi = "call"
            if mhi > 0 and mg_1 == -2: action_mhimai = "call"
            if mhi < 0 and mg_1 == 2: action_mhimai = "put"
            if milhao > 0 and mg_1 == 2: action_milhaomin = "put"
            if milhao < 0 and mg_1 == -2: action_milhaomin = "call"
            if milhao > 0 and mg_1 == -2: action_milhaomax = "call"
            if milhao < 0 and mg_1 == 2: action_milhaomax = "put"
         if modo_entrada == 4:
            mg_1 = vela20 + vela21 + vela22
            if mhi > 0 and mg_1 == 3: action_mhi = "put"
            if mhi < 0 and mg_1 == -3: action_mhi = "call"
            if mhi > 0 and mg_1 == -3: action_mhimai = "call"
            if mhi < 0 and mg_1 == 3: action_mhimai = "put"
            if milhao > 0 and mg_1 == 3: action_milhaomin = "put"
            if milhao < 0 and mg_1 == -3: action_milhaomin = "call"
            if milhao > 0 and mg_1 == -3: action_milhaomax = "call"
            if milhao < 0 and mg_1 == 3: action_milhaomax = "put"
         if modo_entrada == 5:
            mg_1 = vela20 + vela21 + vela22 + vela23
            if mhi > 0 and mg_1 == 4: action_mhi = "put"
            if mhi < 0 and mg_1 == -4: action_mhi = "call"
            if mhi > 0 and mg_1 == -4: action_mhimai = "call"
            if mhi < 0 and mg_1 == 4: action_mhimai = "put"
            if milhao > 0 and mg_1 == 4: action_milhaomin = "put"
            if milhao < 0 and mg_1 == -4: action_milhaomin = "call"
            if milhao > 0 and mg_1 == -4: action_milhaomax = "call"
            if milhao < 0 and mg_1 == 4: action_milhaomax = "put"
         
         if check_lowest == 1 or check_low == 1 or check_normal == 1 or check_high == 1 or check_highest == 1:   
          if action_mhi == "put" and analisis_tecnico == "compra": action_mhi = "none"
          if action_mhi == "call" and analisis_tecnico == "venta": action_mhi = "none"
          if action_mhimai == "put" and analisis_tecnico == "compra": action_mhimai = "none"
          if action_mhimai == "call" and analisis_tecnico == "venta": action_mhimai = "none"
          if action_milhaomin == "put" and analisis_tecnico == "compra": action_milhaomin = "none"
          if action_milhaomin == "call" and analisis_tecnico == "venta": action_milhaomin = "none"
          if action_milhaomax == "put" and analisis_tecnico == "compra": action_milhaomax = "none"
          if action_milhaomax == "call" and analisis_tecnico == "venta": action_milhaomax = "none"
          if analisis_tecnico == "none": 
              action_mhi = "none"
              action_mhimai = "none"
              action_milhaomin = "none"
              action_milhaomax = "none"
              
              
       
         print (estado)
         global alerta_mhi 
         global alerta_mhimai
         if mhi_enter == "stop":
             estado = "desbloquiado"
         
         alerta_mhimai = "go" 
         if mhi_enter == "go" and check_mhi == 1 and action_mhi != "none" and estado == "desbloquiado":
          alerta_mhi = "go"
          hilo_mhi_turbo = threading.Thread(target=turbo_mhi, args=(money,par,martingala,mg_modo,stop_ops))
          hilo_mhi_turbo.start() 
           
         if mhimai_enter == "go" and check_mhimai == 1 and action_mhimai != "none":
             
          hilo_mhimai_turbo = threading.Thread(target=turbo_mhimai, args=(money,par,martingala,mg_modo,stop_ops))
          hilo_mhimai_turbo.start()
 
              
         if milhaomin_enter == "go" and check_milhaomin == 1 and action_milhaomin != "none":
          hilo_milhaomin_turbo = threading.Thread(target=turbo_milhaomin, args=(action_milhaomin,money,par,martingala,mg_modo,stop_ops))
          hilo_milhaomin_turbo.start()
          

         if milhaomax_enter == "go" and check_milhaomax == 1 and action_milhaomax != "none":
          hilo_milhaomax_turbo = threading.Thread(target=turbo_milhaomax, args=(action_milhaomax,money,par,martingala,mg_modo,stop_ops))
          hilo_milhaomax_turbo.start()

          
      if hora_entrar_mhi == 1 + n2 or  hora_entrar_mhi == 6 + n2:
            
         mhi = vela17 + vela18 + vela19 
         padrao23 = vela20
         if modo_entrada == 1:
            if mhi > 0: action_mhi2 = "put"
            if mhi < 0: action_mhi2 = "call"
            if mhi > 0: action_mhi2mai = "call"
            if mhi < 0: action_mhi2mai = "put"
            if padrao23 > 0: action_padrao23 = "call"
            if padrao23 < 0: action_padrao23 = "put"
           
         if modo_entrada == 2:
            mg_2 = vela21 
            if mhi > 0 and mg_2 == 1: action_mhi2 = "put"
            if mhi < 0 and mg_2 == -1: action_mhi2 = "call"
            if mhi > 0 and mg_2 == -1: action_mhi2mai = "call"
            if mhi < 0 and mg_2 == 1: action_mhi2mai = "put"
            if padrao23 > 0 and mg_2 == -1: action_padrao23 = "call"
            if padrao23 < 0 and mg_2 == 1: action_padrao23 = "put"
            
         if modo_entrada == 3:
            mg_2 = vela21 + vela22
            if mhi > 0 and mg_2 == 2: action_mhi2 = "put"
            if mhi < 0 and mg_2 == -2: action_mhi2 = "call"
            if mhi > 0 and mg_2 == -2: action_mhi2mai = "call"
            if mhi < 0 and mg_2 == 2: action_mhi2mai = "put"
            if padrao23 > 0 and mg_2 == -2: action_padrao23 = "call"
            if padrao23 < 0 and mg_2 == 2: action_padrao23 = "put"
            
         if modo_entrada == 4:
            mg_2 = vela21 + vela22 + vela23
            if mhi > 0 and mg_2 == 3: action_mhi2 = "put"
            if mhi < 0 and mg_2 == -3: action_mhi2 = "call"
            if mhi > 0 and mg_2 == -3: action_mhi2mai = "call"
            if mhi < 0 and mg_2 == 3: action_mhi2mai = "put"
            if padrao23 > 0 and mg_2 == -3: action_padrao23 = "call"
            if padrao23 < 0 and mg_2 == 3: action_padrao23 = "put"
            
         if modo_entrada == 5:
            mg_2 = vela21 + vela22 + vela23 + vela24
            if mhi > 0 and mg_2 == 4: action_mhi2 = "put"
            if mhi < 0 and mg_2 == -4: action_mhi2 = "call"
            if mhi > 0 and mg_2 == -4: action_mhi2mai = "call"
            if mhi < 0 and mg_2 == 4: action_mhi2mai = "put"
            if padrao23 > 0 and mg_2 == -4: action_padrao23 = "call"
            if padrao23 < 0 and mg_2 == 4: action_padrao23 = "put"
            
         if check_lowest == 1 or check_low == 1 or check_normal == 1 or check_high == 1 or check_highest == 1:    
          if action_mhi2 == "put" and analisis_tecnico == "compra": action_mhi2 = "none"
          if action_mhi2 == "call" and analisis_tecnico == "venta": action_mhi2 = "none"
          if action_mhi2mai == "put" and analisis_tecnico == "compra": action_mhi2mai = "none"
          if action_mhi2mai == "call" and analisis_tecnico == "venta": action_mhi2mai = "none"
          if action_padrao23 == "put" and analisis_tecnico == "compra": action_padrao23 = "none"
          if action_padrao23 == "call" and analisis_tecnico == "venta": action_padrao23 = "none"
          if analisis_tecnico == "none": 
              action_mhi2 = "none"
              action_mhi2mai = "none"
              action_padrao23 = "none"
          
         global alerta_mhi2 
         global alerta_mhi2mai
         alerta_mhi2 = "go"
         alerta_mhi2mai = "go"      
              
         if mhi2_enter == "go" and check_mhi2 == 1 and action_mhi2 != "none":   
          hilo_mhi2_turbo = threading.Thread(target=turbo_mhi2, args=(money,par,martingala,mg_modo,stop_ops))
          hilo_mhi2_turbo.start()
         if mhi2mai_enter == "go" and check_mhi2mai == 1 and action_mhi2mai != "none":
          hilo_mhi2mai_turbo = threading.Thread(target=turbo_mhi2mai, args=(money,par,martingala,mg_modo,stop_ops))
          hilo_mhi2mai_turbo.start()
         if padrao23_enter == "go" and check_padrao23 == 1 and action_padrao23 != "none":
          hilo_padrao23_turbo = threading.Thread(target=turbo_padrao23, args=(action_padrao23,money,par,martingala,mg_modo,stop_ops))
          hilo_padrao23_turbo.start()
           
      if hora_entrar_mhi == 2 + n3 or  hora_entrar_mhi == 7 + n3:
            
         mhi = vela17 + vela18 + vela19 
         melhor =vela16 + vela17 + vela18
         if modo_entrada == 1:
            if mhi > 0: action_mhi3 = "put"
            if mhi < 0: action_mhi3 = "call"
            if mhi > 0: action_mhi3mai = "call"
            if mhi < 0: action_mhi3mai = "put"
            if melhor > 0: action_melhor = "call"
            if melhor < 0: action_melhor = "put"
           
         if modo_entrada == 2:
            mg_3 = vela22 
            if mhi > 0 and mg_3 == 1: action_mhi3 = "put"
            if mhi < 0 and mg_3 == -1: action_mhi3 = "call"
            if mhi > 0 and mg_3 == -1: action_mhi3mai = "call"
            if mhi < 0 and mg_3 == 1: action_mhi3mai = "put"
            if melhor > 0 and mg_3 == -1: action_melhor = "call"
            if melhor < 0 and mg_3 == 1: action_melhor = "put"
            
         if modo_entrada == 3:
            mg_3 = vela22 + vela23
            if mhi > 0 and mg_3 == 2: action_mhi3 = "put"
            if mhi < 0 and mg_3 == -2: action_mhi3 = "call"
            if mhi > 0 and mg_3 == -2: action_mhi3mai = "call"
            if mhi < 0 and mg_3 == 2: action_mhi3mai = "put"
            if melhor > 0 and mg_3 == -2: action_melhor = "call"
            if melhor < 0 and mg_3 == 2: action_melhor = "put"
            
         if modo_entrada == 4:
            mg_3 = vela22 + vela23 + vela24
            if mhi > 0 and mg_3 == 3: action_mhi3 = "put"
            if mhi < 0 and mg_3 == -3: action_mhi3 = "call"
            if mhi > 0 and mg_3 == -3: action_mhi3mai = "call"
            if mhi < 0 and mg_3 == 3: action_mhi3mai = "put"
            if melhor > 0 and mg_3 == -3: action_melhor = "call"
            if melhor < 0 and mg_3 == 3: action_melhor = "put"
            
         if modo_entrada == 5:
            mg_3 = vela22 + vela23 + vela24 + vela25
            if mhi > 0 and mg_3 == 4: action_mhi3 = "put"
            if mhi < 0 and mg_3 == -4: action_mhi3 = "call"
            if mhi > 0 and mg_3 == -4: action_mhi3mai = "call"
            if mhi < 0 and mg_3 == 4: action_mhi3mai = "put"
            if melhor > 0 and mg_3 == -4: action_melhor = "call"
            if melhor < 0 and mg_3 == 4: action_melhor = "put"
            
         if check_lowest == 1 or check_low == 1 or check_normal == 1 or check_high == 1 or check_highest == 1:    
          if action_mhi3 == "put" and analisis_tecnico == "compra": action_mhi3 = "none"
          if action_mhi3 == "call" and analisis_tecnico == "venta": action_mhi3 = "none"
          if action_mhi3mai == "put" and analisis_tecnico == "compra": action_mhi3mai = "none"
          if action_mhi3mai == "call" and analisis_tecnico == "venta": action_mhi3mai = "none"
          if action_melhor == "put" and analisis_tecnico == "compra": action_melhor = "none"
          if action_melhor == "call" and analisis_tecnico == "venta": action_melhor = "none"
          if analisis_tecnico == "none": 
              action_mhi3 = "none"
              action_mhi3mai = "none"
              action_melhor = "none"
            
         global alerta_mhi3 
         global alerta_mhi3mai
         alerta_mhi3 = "go"
         alerta_mhi3mai = "go" 
         
         if mhi3_enter == "go" and check_mhi3 == 1 and action_mhi3 != "none":    
          hilo_mhi3_turbo = threading.Thread(target=turbo_mhi3, args=(money,par,martingala,mg_modo,stop_ops)) 
          hilo_mhi3_turbo.start()
          
         if mhi3mai_enter == "go" and check_mhi3mai == 1 and action_mhi3mai != "none":
          hilo_mhi3mai_turbo = threading.Thread(target=turbo_mhi3mai, args=(money,par,martingala,mg_modo,stop_ops)) 
          hilo_mhi3mai_turbo.start()
          
         if melhor_enter == "go" and check_melhor == 1 and action_melhor != "none":
          hilo_melhor_turbo = threading.Thread(target=turbo_melhor, args=(action_melhor,money,par,martingala,mg_modo,stop_ops)) 
          hilo_melhor_turbo.start()
          
      if hora_entrar_mhi == 4 + n4 or  hora_entrar_mhi == 9 + n4:       
         torres = vela15
         padrao3x1 = vela15 + vela16 + vela17
         if modo_entrada == 1:
            if torres > 0: action_torres = "call"
            if torres < 0: action_torres = "put"
            if padrao3x1 > 0: action_padrao3x1 = "put"
            if padrao3x1 < 0: action_padrao3x1 = "call"          
           
         if modo_entrada == 2:
            mg_4 = vela19
            if torres > 0 and mg_4 == -1: action_torres = "call"
            if torres < 0 and mg_4 == 1: action_torres = "put"
            if padrao3x1 > 0 and mg_4 == 1: action_padrao3x1 = "put"
            if padrao3x1 < 0 and mg_4 == -1: action_padrao3x1 = "call"
            
         if modo_entrada == 3:
            mg_4 = vela19 + vela20
            if torres > 0 and mg_4 == -2: action_torres = "call"
            if torres < 0 and mg_4 == 2: action_torres = "put"
            if padrao3x1 > 0 and mg_4 == 2: action_padrao3x1 = "put"
            if padrao3x1 < 0 and mg_4 == -2: action_padrao3x1 = "call"
            
         if modo_entrada == 4:
            mg_4 = vela19 + vela20 + vela21
            if torres > 0 and mg_4 == -3: action_torres = "call"
            if torres < 0 and mg_4 == 3: action_torres = "put"
            if padrao3x1 > 0 and mg_4 == 3: action_padrao3x1 = "put"
            if padrao3x1 < 0 and mg_4 == -3: action_padrao3x1 = "call"
            
         if modo_entrada == 5:
            mg_4 = vela19 + vela20 + vela21 + vela22
            if torres > 0 and mg_4 == -4: action_torres = "call"
            if torres < 0 and mg_4 == 4: action_torres = "put"
            if padrao3x1 > 0 and mg_4 == 4: action_padrao3x1 = "put"
            if padrao3x1 < 0 and mg_4 == -4: action_padrao3x1 = "call"
            
         if check_lowest == 1 or check_low == 1 or check_normal == 1 or check_high == 1 or check_highest == 1: 
          if action_torres == "put" and analisis_tecnico == "compra": action_torres = "none"
          if action_torres == "call" and analisis_tecnico == "venta": action_torres = "none"
          if action_padrao3x1 == "put" and analisis_tecnico == "compra": action_padrao3x1 = "none"
          if action_padrao3x1 == "call" and analisis_tecnico == "venta": action_padrao3x1 = "none"
          if analisis_tecnico == "none": 
              action_torres = "none"
              action_padrao3x1 = "none"
          
         if torres_enter == "go" and check_torres == 1 and action_torres!= "none":    
          hilo_torres_turbo = threading.Thread(target=turbo_mhi3, args=(action_torres,money,par,martingala,mg_modo,stop_ops)) 
          hilo_torres_turbo.start()
         if padrao3x1_enter == "go" and check_padrao3x1 == 1 and action_padrao3x1 != "none":
          hilo_padrao3x1_turbo = threading.Thread(target=turbo_padrao3x1, args=(action_padrao3x1,money,par,martingala,mg_modo,stop_ops)) 
          hilo_padrao3x1_turbo.start()
 
        
def turbo_mhi(money3,par,martingala,mg_modo,stop_ops):
 n = 0 
 action = "none"
 fin = "none"
 money = money3
 money2 = money3
 while n < 1: 
     if fin == "true": break
     n = n + 1     
     global n_operaciones
     global alerta_mhi    
     global n_operaciones
     global action_mhi
     global estado
     estado = "bloquiado"
     action = action_mhi
     if n_operaciones < stop_ops or stop_ops == 0:
       n_operaciones = n_operaciones + 1    
       check_status = []
       mg_count = 0
       if mg_modo != 2:
        money = money3
        money2 = money3
       if mg_modo == 2: mg_count = 0 
       envio1 = 0.0
       global profit5
       while True:
           if alerta_mhi == "go":
               break
           time.sleep(0.1)
           
       while True:
         if mg_count > martingala:
             graf_panel5("Operacion MHI loose" )
             if mg_modo == 0:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
              modo_turbo_score(0,1,envio1)
              fin = "true"
              
             if mg_modo == 1:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
              modo_turbo_score(0,1,envio1)
              fin = "true"
              
             if mg_modo == 2 and n == 9: 
                 if martingala == 0: envio1 = (money2 * (-1))
                 if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5))) * 90
                 if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
                 if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
                 if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
                 if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31))))
                 
                 
                 modo_turbo_score(0,1,envio1) 
                 fin = "true"
             break
         
         print(money)
         print(par)  
         print(action)
         check,turbo = api.buy(money,par,action,1)
        
         if check: 
            graf_panel5("sell/buy realizada" )
         else: 
           graf_panel5("sell/buy fallida" )
           break     
         time.sleep(40)
         alerta_mhi = "none"
         while True:
             now = datetime.now()
             seg = format(now.second)
             if seg == "0": break
             time.sleep(0.1)    
         check_status = api.check_win_v4(turbo)
         if check_status[0] == "loose" or check_status[0] == "equal":    
           if mg_modo == 0 or mg_modo == 2:
            plus = 2 + profit5
           if mg_modo == 1:
            if mg_count == 0:    
             plus = 1 + profit5
            if mg_count > 0:    
             plus = 0 + profit5 
           money = money *  plus
         
         if check_status[0] == "win":
           fin = "true"
           graf_panel5("Operacion MHI Win" )
           modo_turbo_score(1,0, money2 * (1 - profit5))
           break
         mg_count = mg_count + 1


def turbo_mhi2(money3,par,martingala,mg_modo,stop_ops):
 n = 0 
 action = "none"
 while n < 1: 
     n = n + 1
     global n_operaciones
     global alerta_mhi2    
     global n_operaciones
     global action_mhi2
     action = action_mhi2
     if n_operaciones < stop_ops or stop_ops == 0:
       n_operaciones = n_operaciones + 1    
       check_status = []
       mg_count = 0
       money = money3
       money2 = money3
       envio1 = 0.0
       global profit5
       while True:
           if alerta_mhi2 == "go":
               break
           time.sleep(0.1)
           
       while True:
         if mg_count > martingala:
             graf_panel5("Operacion MHI2 loose" )
             if mg_modo == 0:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
             if mg_modo == 1:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
             modo_turbo_score(0,1,envio1)
             break
     
         check,turbo = api.buy(money,par,action,1)
        
         if check: 
            graf_panel5("sell/buy realizada" )
         else: 
           graf_panel5("sell/buy fallida" )
           break     
         time.sleep(40)
         alerta_mhi2 = "none"
         while True:
             now = datetime.now()
             seg = format(now.second)
             if seg == "0": break
             time.sleep(0.1)    
         check_status = api.check_win_v4(turbo)
         if check_status[0] == "loose" or check_status[0] == "equal":  
           if mg_modo == 0:
            plus = 2 + profit5
           if mg_modo == 1:
            if mg_count == 0:    
             plus = 1 + profit5
            if mg_count > 0:    
             plus = 0 + profit5 
           money = money *  plus
           
         
         if check_status[0] == "win":
           graf_panel5("Operacion MHI2 Win" )
           modo_turbo_score(1,0, money2 * (1 - profit5))
           break
         mg_count = mg_count + 1
         
         
         
def turbo_mhi3(money3,par,martingala,mg_modo,stop_ops):
 n = 0 
 action = "none"
 while n < 1: 
     n = n + 1
     global n_operaciones
     global alerta_mhi3    
     global n_operaciones
     global action_mhi3
     action = action_mhi3
     if n_operaciones < stop_ops or stop_ops == 0:
       n_operaciones = n_operaciones + 1    
       check_status = []
       mg_count = 0
       money = money3
       money2 = money3
       envio1 = 0.0
       global profit5
       while True:
           if alerta_mhi3 == "go":
               break
           time.sleep(0.1)
           
       while True:
         if mg_count > martingala:
             graf_panel5("Operacion MHI3 loose" )
             if mg_modo == 0:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
             if mg_modo == 1:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
             modo_turbo_score(0,1,envio1)
             break

         check,turbo = api.buy(money,par,action,1)
        
         if check: 
            graf_panel5("sell/buy realizada" )
         else: 
           graf_panel5("sell/buy fallida" )
           break     
         time.sleep(40)
         alerta_mhi3 = "none"
         while True:
             now = datetime.now()
             seg = format(now.second)
             if seg == "0": break
             time.sleep(0.1)    
         check_status = api.check_win_v4(turbo)
         if check_status[0] == "loose" or check_status[0] == "equal":  
           if mg_modo == 0:
            plus = 2 + profit5
           if mg_modo == 1:
            if mg_count == 0:    
             plus = 1 + profit5
            if mg_count > 0:    
             plus = 0 + profit5 
           money = money *  plus
           
         
         if check_status[0] == "win":
           graf_panel5("Operacion MHI3 Win" )
           modo_turbo_score(1,0, money2 * (1 - profit5))
           break
         mg_count = mg_count + 1 
         
def turbo_mhimai(money3,par,martingala,mg_modo,stop_ops):
 n = 0 
 action = "none"
 while n < 1: 
     n = n + 1
     global n_operaciones
     global alerta_mhimai    
     global n_operaciones
     global action_mhimai
     action = action_mhimai
     if n_operaciones < stop_ops or stop_ops == 0:
       n_operaciones = n_operaciones + 1    
       check_status = []
       mg_count = 0
       money = money3
       money2 = money3
       envio1 = 0.0
       global profit5
       while True:
           if alerta_mhimai == "go":
               break
           time.sleep(0.1)
           
       while True:
         if mg_count > martingala:
             graf_panel5("Operacion MHIMAI loose" )
             if mg_modo == 0:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
             if mg_modo == 1:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
             modo_turbo_score(0,1,envio1)
             break
   
         check,turbo = api.buy(money,par,action,1)
        
         if check: 
            graf_panel5("sell/buy realizada" )
         else: 
           graf_panel5("sell/buy fallida" )
           break     
         time.sleep(40)
         alerta_mhimai = "none"
         while True:
             now = datetime.now()
             seg = format(now.second)
             if seg == "0": break
             time.sleep(0.1)    
         check_status = api.check_win_v4(turbo)
         if check_status[0] == "loose" or check_status[0] == "equal":  
           if mg_modo == 0:
            plus = 2 + profit5
           if mg_modo == 1:
            if mg_count == 0:    
             plus = 1 + profit5
            if mg_count > 0:    
             plus = 0 + profit5 
           money = money *  plus
           
         
         if check_status[0] == "win":
           graf_panel5("Operacion MHIMAI Win" )
           modo_turbo_score(1,0, money2 * (1 - profit5))
           break
         mg_count = mg_count + 1         
         
def turbo_mhi2mai(money3,par,martingala,mg_modo,stop_ops):
 n = 0 
 action = "none"
 while n < 1: 
     n = n + 1
     global n_operaciones
     global alerta_mhi2mai    
     global n_operaciones
     global action_mhi2mai
     action = action_mhi2mai
     if n_operaciones < stop_ops or stop_ops == 0:
       n_operaciones = n_operaciones + 1    
       check_status = []
       mg_count = 0
       money = money3
       money2 = money3
       envio1 = 0.0
       global profit5
       while True:
           if alerta_mhi2mai == "go":
               break
           time.sleep(0.1)
           
       while True:
         if mg_count > martingala:
             graf_panel5("Operacion MHI2MAI loose" )
             if mg_modo == 0:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
             if mg_modo == 1:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
             modo_turbo_score(0,1,envio1)
             break
      
         check,turbo = api.buy(money,par,action,1)
        
         if check: 
            graf_panel5("sell/buy realizada" )
         else: 
           graf_panel5("sell/buy fallida" )
           break     
         time.sleep(40)
         alerta_mhi2mai = "none"
         while True:
             now = datetime.now()
             seg = format(now.second)
             if seg == "0": break
             time.sleep(0.1)    
         check_status = api.check_win_v4(turbo)
         if check_status[0] == "loose" or check_status[0] == "equal":  
           if mg_modo == 0:
            plus = 2 + profit5
           if mg_modo == 1:
            if mg_count == 0:    
             plus = 1 + profit5
            if mg_count > 0:    
             plus = 0 + profit5 
           money = money *  plus
           
         
         if check_status[0] == "win":
           graf_panel5("Operacion MHI2MAI Win" )
           modo_turbo_score(1,0, money2 * (1 - profit5))
           break
         mg_count = mg_count + 1
         
         
def turbo_mhi3mai(money3,par,martingala,mg_modo,stop_ops):
 n = 0 
 action = "none"
 while n < 1: 
     n = n + 1
     global n_operaciones
     global alerta_mhi3mai    
     global n_operaciones
     global action_mhi3mai
     action = action_mhi3mai
     if n_operaciones < stop_ops or stop_ops == 0:
       n_operaciones = n_operaciones + 1    
       check_status = []
       mg_count = 0
       money = money3
       money2 = money3
       envio1 = 0.0
       global profit5
       while True:
           if alerta_mhi3mai == "go":
               break
           time.sleep(0.1)
           
       while True:
         if mg_count > martingala:
             graf_panel5("Operacion MHI3MAI loose" )
             if mg_modo == 0:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
             if mg_modo == 1:
              if martingala == 0: envio1 = (money2 * (-1))
              if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
              if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
              if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
              if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
              if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
             modo_turbo_score(0,1,envio1)
             break
     
         check,turbo = api.buy(money,par,action,1)
        
         if check: 
            graf_panel5("sell/buy realizada" )
         else: 
           graf_panel5("sell/buy fallida" )
           break     
         time.sleep(40)
         alerta_mhi3mai = "none"
         while True:
             now = datetime.now()
             seg = format(now.second)
             if seg == "0": break
             time.sleep(0.1)    
         check_status = api.check_win_v4(turbo)
         if check_status[0] == "loose" or check_status[0] == "equal":  
           if mg_modo == 0:
            plus = 2 + profit5
           if mg_modo == 1:
            if mg_count == 0:    
             plus = 1 + profit5
            if mg_count > 0:    
             plus = 0 + profit5 
           money = money *  plus
           
         
         if check_status[0] == "win":
           graf_panel5("Operacion MHI3MAI Win" )
           modo_turbo_score(1,0, money2 * (1 - profit5))
           break
         mg_count = mg_count + 1         
        
def turbo_milhaomin(action,money,par,martingala,mg_modo,stop_ops):
 global n_operaciones
 if n_operaciones < stop_ops or stop_ops == 0:
   n_operaciones = n_operaciones + 1    
   check_status = []
   mg_count = 0
   money2 = money
   envio1 = 0.0
   global profit5
   while True:
    if mg_count > martingala:
        graf_panel5("Operacion Milhao-min loose" )
        if mg_modo == 0:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
        if mg_modo == 1:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
        modo_turbo_score(0,1,envio1)
        break
    check,turbo7 = api.buy(money,par,action,1)
   
    if check: 
       graf_panel5("sell/buy realizada" )
    else: 
      graf_panel5("sell/buy fallida" )
      break     
    time.sleep(40)
    while True:
        now = datetime.now()
        seg = format(now.second)
        if seg == "0": break
        time.sleep(0.2)    
    check_status = api.check_win_v4(turbo7)
    if check_status[0] == "loose":  
      if mg_modo == 0:
       plus = 2 + profit5
      if mg_modo == 1:
       if mg_count == 0:    
        plus = 1 + profit5
       if mg_count > 0:    
        plus =  + profit5 
      money = money *  plus
      
    else:
     if check_status[0] == "win":
      graf_panel5("Operacion Milhao-min Win" )
      modo_turbo_score(1,0, money2 * (1 - profit5))
      break
     else: graf_panel5("Operacion Milhao-min Equal" )
     break
    mg_count = mg_count + 1  
            
        
def turbo_milhaomax(action,money,par,martingala,mg_modo,stop_ops): 
 global n_operaciones
 if n_operaciones < stop_ops or stop_ops == 0:
    n_operaciones = n_operaciones + 1    
    check_status = []
    mg_count = 0
    money2 = money
    envio1 = 0.0
    global profit5
    while True:
      if mg_count > martingala:
          graf_panel5("Operacion Milhao-max loose" )
          if mg_modo == 0:
           if martingala == 0: envio1 = (money2 * (-1))
           if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
           if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
           if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
           if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
           if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
          if mg_modo == 1:
           if martingala == 0: envio1 = (money2 * (-1))
           if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
           if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
           if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
           if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
           if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
          modo_turbo_score(0,1,envio1)
          break
      check,turbo8 = api.buy(money,par,action,1)
     
      if check: 
         graf_panel5("sell/buy realizada" )
      else: 
        graf_panel5("sell/buy fallida" )
        break     
      time.sleep(40)
      while True:
          now = datetime.now()
          seg = format(now.second)
          if seg == "0": break
          time.sleep(0.2)    
      check_status = api.check_win_v4(turbo8)
      if check_status[0] == "loose":  
        if mg_modo == 0:
         plus = 2 + profit5
        if mg_modo == 1:
         if mg_count == 0:    
          plus = 1 + profit5
         if mg_count > 0:    
          plus =  + profit5 
        money = money *  plus
        
      else:
       if check_status[0] == "win":
        graf_panel5("Operacion Milhao-max Win" )
        modo_turbo_score(1,0, money2 * (1 - profit5))
        break
       else: graf_panel5("Operacion Milhao-max Equal" )
       break
      mg_count = mg_count + 1          
        
        
def turbo_torres(action,money,par,martingala,mg_modo,stop_ops):
 global n_operaciones
 if n_operaciones < stop_ops or stop_ops == 0:
   n_operaciones = n_operaciones + 1    
   check_status = []
   mg_count = 0
   money2 = money
   envio1 = 0.0
   global profit5
   while True:
    if mg_count > martingala:
        graf_panel5("Operacion Torres loose" )
        if mg_modo == 0:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
        if mg_modo == 1:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
        modo_turbo_score(0,1,envio1)
        break
    check,turbo9 = api.buy(money,par,action,1)
   
    if check: 
       graf_panel5("sell/buy realizada" )
    else: 
      graf_panel5("sell/buy fallida" )
      break     
    time.sleep(40)
    while True:
        now = datetime.now()
        seg = format(now.second)
        if seg == "0": break
        time.sleep(0.2)    
    check_status = api.check_win_v4(turbo9)
    if check_status[0] == "loose":  
      if mg_modo == 0:
       plus = 2 + profit5
      if mg_modo == 1:
       if mg_count == 0:    
        plus = 1 + profit5
       if mg_count > 0:    
        plus =  + profit5 
      money = money *  plus
      
    else:
     if check_status[0] == "win":
      graf_panel5("Operacion Torres Win" )
      modo_turbo_score(1,0, money2 * (1 - profit5))
      break
     else: graf_panel5("Operacion Torres Equal" )
     break
    mg_count = mg_count + 1                  
        
        
def turbo_padrao23(action,money,par,martingala,mg_modo,stop_ops): 
 global n_operaciones
 if n_operaciones < stop_ops or stop_ops == 0:
   n_operaciones = n_operaciones + 1    
   check_status = []
   mg_count = 0
   money2 = money
   envio1 = 0.0
   global profit5
   while True:
    if mg_count > martingala:
        graf_panel5("Operacion Padrao23 loose" )
        if mg_modo == 0:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
        if mg_modo == 1:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
        modo_turbo_score(0,1,envio1)
        break
    check,turbo10 = api.buy(money,par,action,1)
   
    if check: 
       graf_panel5("sell/buy realizada" )
    else: 
      graf_panel5("sell/buy fallida" )
      break     
    time.sleep(40)
    while True:
        now = datetime.now()
        seg = format(now.second)
        if seg == "0": break
        time.sleep(0.2)    
    check_status = api.check_win_v4(turbo10)
    if check_status[0] == "loose":  
      if mg_modo == 0:
       plus = 2 + profit5
      if mg_modo == 1:
       if mg_count == 0:    
        plus = 1 + profit5
       if mg_count > 0:    
        plus =  + profit5 
      money = money *  plus
      
    else:
     if check_status[0] == "win":
      graf_panel5("Operacion Padrao23 Win" )
      modo_turbo_score(1,0, money2 * (1 - profit5))
      break
     else: graf_panel5("Operacion Padrao23 Equal" )
     break
    mg_count = mg_count + 1   
               
                
def turbo_melhor(action,money,par,martingala,mg_modo,stop_ops): 
 global n_operaciones
 if n_operaciones < stop_ops or stop_ops == 0:
   n_operaciones = n_operaciones + 1    
   check_status = []
   mg_count = 0
   money2 = money
   envio1 = 0.0
   global profit5
   while True:
    if mg_count > martingala:
        graf_panel5("Operacion Melhor loose" )
        if mg_modo == 0:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
        if mg_modo == 1:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
        modo_turbo_score(0,1,envio1)
        break
    check,turbo11 = api.buy(money,par,action,1)
   
    if check: 
       graf_panel5("sell/buy realizada" )
    else: 
      graf_panel5("sell/buy fallida" )
      break     
    time.sleep(40)
    while True:
        now = datetime.now()
        seg = format(now.second)
        if seg == "0": break
        time.sleep(0.2)    
    check_status = api.check_win_v4(turbo11)
    if check_status[0] == "loose":  
      if mg_modo == 0:
       plus = 2 + profit5
      if mg_modo == 1:
       if mg_count == 0:    
        plus = 1 + profit5
       if mg_count > 0:    
        plus =  + profit5 
      money = money *  plus
      
    else:
     if check_status[0] == "win":
      graf_panel5("Operacion Melhor Win" )
      modo_turbo_score(1,0, money2 * (1 - profit5))
      break
     else: graf_panel5("Operacion Melhor Equal" )
     break
    mg_count = mg_count + 1                          
        
        
def turbo_padrao3x1(action,money,par,martingala,mg_modo,stop_ops):
 global n_operaciones
 if n_operaciones < stop_ops or stop_ops == 0:
   n_operaciones = n_operaciones + 1    
   check_status = []
   mg_count = 0
   money2 = money
   envio1 = 0.0
   global profit5
   while True:
    if mg_count > martingala:
        graf_panel5("Operacion Padrao3x1 loose" )
        if mg_modo == 0:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(3 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(7 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(15 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(31 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(63 + (profit5 * 31)))) 
        if mg_modo == 1:
         if martingala == 0: envio1 = (money2 * (-1))
         if martingala == 1: envio1 = (-1 *(money2 *(2 + profit5)))
         if martingala == 2: envio1 = (-1 *(money2 *(4 + (profit5 * 3))))
         if martingala == 3: envio1 = (-1 *(money2 *(8 + (profit5 * 7))))
         if martingala == 4: envio1 = (-1 *(money2 *(16 + (profit5 * 15))))
         if martingala == 5: envio1 = (-1 *(money2 *(32 + (profit5 * 31)))) 
        modo_turbo_score(0,1,envio1)
        break
    check,turbo12 = api.buy(money,par,action,1)
   
    if check: 
       graf_panel5("sell/buy realizada" )
    else: 
      graf_panel5("sell/buy fallida" )
      break     
    time.sleep(40)
    while True:
        now = datetime.now()
        seg = format(now.second)
        if seg == "0": break
        time.sleep(0.1)    
    check_status = api.check_win_v4(turbo12)
    if check_status[0] == "loose":  
      if mg_modo == 0:
       plus = 2 + profit5
      if mg_modo == 1:
       if mg_count == 0:    
        plus = 1 + profit5
       if mg_count > 0:    
        plus =  + profit5 
      money = money *  plus
      
    else:
     if check_status[0] == "win":
      graf_panel5("Operacion Padrao3x1 Win" )
      modo_turbo_score(1,0, money2 * (1 - profit5))
      break
     else: graf_panel5("Operacion Padrao3x1 Equal" )
     break
    mg_count = mg_count + 1                     
        
        
    

ganadas_turbo = 0
perdidas_turbo = 0      
def modo_turbo_score(ganadast,perdidast,envios):
  global ganadas_turbo 
  global perdidas_turbo
  ganadas_turbo = ganadas_turbo + ganadast
  perdidas_turbo = perdidas_turbo + perdidast

  graf_panel5_score(ganadas_turbo,perdidas_turbo)
  graf_global()
  ganancias_totales(envios)
  
      
######################################################ASSETS STATUS####################################################



status_global_win2 = "0"
status_global_loose2 = "0"

on_p1= 1
on_p2= 1
on_p3= 1
on_p4= 1
status_p1_win = 0 
status_p1_loose = 0 
status_p2_win = 0
status_p2_loose = 0 
status_p3_win = 0
status_p3_loose = 0 
status_p4_win = 0 
status_p4_loose = 0 
status_p5_win = 0
status_p5_loose = 0

app = Tk()
app.title("ELIBOT")
app.geometry('1366x704')
app.state('zoomed')

####################IMAGENES#########################
imagen=PhotoImage(file="fondo.gif")
color_fondo = '#191f2d'
color_fondo2 = '#131722'
color_mamey = '#ff7700'
color_fondo3 = '#c8cad0'
color_turbo = '#c57a38'
divisa = ["assets"]

nzdusd_otc_foto=PhotoImage(file="images/nzdusd-otc.png")
audcad_otc_foto=PhotoImage(file="images/audcad-otc.png")
eurusd_otc_foto=PhotoImage(file="images/eurusd-otc.png")
usdinr_otc_foto=PhotoImage(file="images/usdinr-otc.png")
usdzar_otc_foto=PhotoImage(file="images/usdzar-otc.png")
usdhkd_otc_foto=PhotoImage(file="images/usdhkd-otc.png")
usdchf_otc_foto=PhotoImage(file="images/usdchf-otc.png")
usdsgd_otc_foto=PhotoImage(file="images/usdsgd-otc.png")
eurgbp_otc_foto=PhotoImage(file="images/eurgbp-otc.png")
gbpusd_otc_foto=PhotoImage(file="images/gbpusd-otc.png")
eurjpy_otc_foto=PhotoImage(file="images/eurjpy-otc.png")
gbpjpy_foto=PhotoImage(file="images/gbpjpy.png")
audcad_foto=PhotoImage(file="images/audcad.png")
eurusd_foto=PhotoImage(file="images/eurusd.png")
audjpy_foto=PhotoImage(file="images/audjpy.png")
usdjpy_foto=PhotoImage(file="images/usdjpy.png")
audusd_foto=PhotoImage(file="images/audusd.png")
btcusd_foto=PhotoImage(file="images/btcusd.png")
ethusd_foto=PhotoImage(file="images/ethusd.png")
xrpusd_foto=PhotoImage(file="images/xrpusd.png")
eurgbp_foto=PhotoImage(file="images/eurgbp.png")
gbpusd_foto=PhotoImage(file="images/gbpusd.png")
eurjpy_foto=PhotoImage(file="images/eurjpy.png")
default_foto=PhotoImage(file="images/default.png")

btn_assets_foto=PhotoImage(file="btn_assets.png")
btn_entrar_foto=PhotoImage(file="entrar.png")
inicio_entrar_foto=PhotoImage(file="inicio_entrar.png")
on=PhotoImage(file="on.png")
off=PhotoImage(file="off.png")
on2=PhotoImage(file="on2.png")
off2=PhotoImage(file="off2.png")
on3=PhotoImage(file="on3.png")
off3=PhotoImage(file="off3.png")
start=PhotoImage(file="start.png")
stop=PhotoImage(file="stop.png")
start2=PhotoImage(file="start2.png")
stop2=PhotoImage(file="stop2.png")
lblImagen=Label(app,image=imagen).place(x=0, y=0)


###############################CONEXION######################################################  
status_conect = Label(text= "Por favor conecte a IQ Option", bg = color_fondo, fg = "white")
status_conect.place(x=830, y=58)
status_conect.config(font=('Arial',10))

def conexion_check(): 
  global api  
  while True: 
    try:  
        if api.check_connect() == False:
            status_conect.config(text = "Intentando reconectar")
            api.connect()
        else:
            status_conect.config(text = "Conectado correctamente a IQ Option")
        time.sleep(7) 
    except:
        status_conect.config(text = "Intentando reconectar")
        time.sleep(7) 
            
def start_conexion_check():
	thread = threading.Thread(target=conexion_check)
	thread.start()
 
def conexion_iq(correo,contra):
 global api   
 api = IQ_Option(correo,contra)
 check = api.connect()
 if check:
  start_conexion_check()   
  start_balance()
  
def start_conexion_iq():
    
  conexion = threading.Thread(target=conexion_iq, args = (correo.get(),contra.get()))
  conexion.start()  
  conexion.join()
  
  hilo_auto = threading.Thread(target=procesos_automaticos)
  hilo_auto.start()  
  
  
###########################ENTRADAS DE CREDENCIALES#######################################################################

correo = Entry(width=37, textvariable= "email")
correo.place(x=728, y=30)

contra = Entry(width=35, textvariable= "pass")
contra.place(x=1012, y=30)

btn_entrar_iq = Button(borderwidth = 0, image=btn_entrar_foto, bg = color_fondo,command=lambda:[app.after(200,start_conexion_iq),app.after(200,guardar_credenciales)])
btn_entrar_iq.place(x=1250, y=13)
     
def guardar_credenciales():
  if check_credenciales_var.get() == 1:  
   file = open("config/Readme.txt", "w") 
   file.write(correo.get()+"\n")
   file.write(contra.get())
   file.close()
  else: 
   file = open("config/Readme.txt", "w") 
   file.write(""+"\n")
   file.write("")
   file.close()


    
    
    
file = open("config/Readme.txt", "r")
credenciales_get = file.readlines()
file.close()
count_credenciales = len(credenciales_get)
if count_credenciales >= 1:
 correo_default=credenciales_get[0][:-1]   
 correo.insert(0,correo_default) 
if count_credenciales >= 2:
 contra.insert(0,credenciales_get[1]) 
###########################################################CHECK ANALISIS TECNICO###################################
on_panel_analisis = Button(borderwidth = 0, image=off3, bg = color_fondo)
on_panel_analisis.place(x=255+360, y=32)

paso_analisis1 = "go"
paso_analisis2 = "go"
paso_analisis3 = "go"
paso_analisis4 = "go"
paso_analisis5 = "go"
paso_analisis1 = "go"

def boton_on_off_analisis():
  global paso_analisis1
  global paso_analisis2
  global paso_analisis3
  global paso_analisis4
  global paso_analisis5
  if paso_analisis1 == "go":
   if check_lowest_var.get() == 1:
      check_low_var.set(0)
      check_normal_var.set(0)
      check_high_var.set(0)
      check_highest_var.set(0)
      paso_analisis1 = "stop"
      paso_analisis2 = "go"
      paso_analisis3 = "go"
      paso_analisis4 = "go"
      paso_analisis5 = "go"
      
  if paso_analisis2 == "go":    
   if check_low_var.get()  == 1:
      check_lowest_var.set(0)
      check_normal_var.set(0)
      check_high_var.set(0)
      check_highest_var.set(0)  
      paso_analisis1 = "go"
      paso_analisis2 = "stop"
      paso_analisis3 = "go"
      paso_analisis4 = "go"
      paso_analisis5 = "go"
      
  if paso_analisis3 == "go":   
   if check_normal_var.get()  == 1:
      check_lowest_var.set(0)
      check_low_var.set(0)
      check_high_var.set(0)
      check_highest_var.set(0)
      paso_analisis1 = "go"
      paso_analisis2 = "go"
      paso_analisis3 = "stop"
      paso_analisis4 = "go"
      paso_analisis5 = "go"
      
  if paso_analisis4 == "go":   
   if check_high_var.get()  == 1:
      check_lowest_var.set(0)
      check_low_var.set(0)
      check_normal_var.set(0)
      check_highest_var.set(0)
      paso_analisis1 = "go"
      paso_analisis2 = "go"
      paso_analisis3 = "go"
      paso_analisis4 = "stop"
      paso_analisis5 = "go"
      
  if paso_analisis5 == "go":   
   if check_highest_var.get()  == 1:
      check_lowest_var.set(0)
      check_low_var.set(0)
      check_normal_var.set(0)
      check_high_var.set(0)
      paso_analisis1 = "go"
      paso_analisis2 = "go"
      paso_analisis3 = "go"
      paso_analisis4 = "go"
      paso_analisis5 = "stop"
       
  if  check_lowest_var.get()  == 1 or check_low_var.get()  == 1 or check_normal_var.get()  == 1  or check_high_var.get()  == 1 or check_highest_var.get()  == 1:  
       on_panel_analisis.config(image=on3)
  else: on_panel_analisis.config(image=off3) 
   
check_lowest_var = IntVar()
check_low_var = IntVar()
check_normal_var = IntVar()
check_high_var = IntVar()
check_highest_var = IntVar()


check_lowest = Checkbutton(borderwidth = 0,bg = color_fondo,activebackground = color_fondo,variable = check_lowest_var,command = boton_on_off_analisis)
check_lowest.place(x=385, y=54)

check_low = Checkbutton(borderwidth = 0 , bg = color_fondo,activebackground = color_fondo,variable = check_low_var, command = boton_on_off_analisis)
check_low.place(x=385+44, y=54)

check_normal = Checkbutton(borderwidth = 0,bg = color_fondo,activebackground = color_fondo,variable = check_normal_var, command =boton_on_off_analisis)
check_normal.place(x=385+89, y=54)

check_high = Checkbutton(borderwidth = 0,bg = color_fondo,activebackground = color_fondo,variable = check_high_var, command =boton_on_off_analisis)
check_high.place(x=385+138, y=54)

check_highest = Checkbutton(borderwidth = 0,bg = color_fondo,activebackground = color_fondo,variable = check_highest_var, command =boton_on_off_analisis)
check_highest.place(x=385+182, y=54)


check_credenciales_var = IntVar()
check_credenciales_var.set(1)
check_credenciales = Checkbutton(bg = color_fondo,activebackground = color_fondo,variable = check_credenciales_var)
check_credenciales.place(x=1065, y=50)
################################################CHECK DE ESTRATEGIAS##################################################
def seleted_estrategias():
  if check_mhi_var.get() == 1 or check_mhi2_var.get() == 1 or check_mhi3_var.get() == 1 or check_mhimai_var.get() ==  1 or check_mhi2mai_var.get() == 1 or check_mhi3mai_var.get() == 1 or check_milhaomin_var.get() == 1 or check_milhaomax_var.get() == 1 or check_torres_var.get() == 1 or check_padrao23_var.get() == 1 or check_melhor_var.get() == 1 or check_padrao3x1_var.get() == 1:   
   if divisa[0] != "assets":
     start_panel5.config(state="normal")
  else: 
    start_panel5.config(state="disabled")        

check_mhi_var = IntVar()
check_mhi2_var = IntVar()
check_mhi3_var = IntVar()
check_mhimai_var = IntVar()
check_mhi2mai_var = IntVar()
check_mhi3mai_var = IntVar()
check_milhaomin_var = IntVar()
check_milhaomax_var = IntVar()
check_torres_var = IntVar()
check_padrao23_var = IntVar()
check_melhor_var = IntVar()
check_padrao3x1_var = IntVar()
check_all_var = IntVar()
################################################CHECK DE ESTRATEGIAS##################################################
check_mhi = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_mhi_var , command = seleted_estrategias)
check_mhi.place(x=151, y=341)
check_mhi2 = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_mhi2_var, command = seleted_estrategias)
check_mhi2.place(x=151+210, y=341)
check_mhi3 = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_mhi3_var, command = seleted_estrategias)
check_mhi3.place(x=151+420, y=341)
check_mhimai = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_mhimai_var, command = seleted_estrategias)
check_mhimai.place(x=151+630, y=341)
check_mhi2mai = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_mhi2mai_var, command = seleted_estrategias)
check_mhi2mai.place(x=151+840, y=341)
check_mhi3mai = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_mhi3mai_var, command = seleted_estrategias)
check_mhi3mai.place(x=151+1050, y=341)

check_milhaomin = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_milhaomin_var, command = seleted_estrategias)
check_milhaomin.place(x=151, y=341+185)
check_milhaomax = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_milhaomax_var, command = seleted_estrategias)
check_milhaomax.place(x=151+210, y=341+185)
check_torres = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_torres_var, command = seleted_estrategias)
check_torres.place(x=151+420, y=341+185)
check_padrao23 = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_padrao23_var, command = seleted_estrategias)
check_padrao23.place(x=151+630, y=341+185)
check_melhor = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_melhor_var, command = seleted_estrategias)
check_melhor.place(x=151+840, y=341+185)
check_padrao3x1 = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_padrao3x1_var, command = seleted_estrategias)
check_padrao3x1.place(x=151+1050, y=341+185)
   
def seleccionar_todo():
  if check_all_var.get() == 1:
      check_mhi_var.set(1)
      check_mhi2_var.set(1)
      check_mhi3_var.set(1)
      check_mhimai_var.set(1)
      check_mhi2mai_var.set(1)
      check_mhi3mai_var.set(1)
      check_milhaomin_var.set(1)
      check_milhaomax_var.set(1)
      check_torres_var.set(1)
      check_padrao23_var.set(1)
      check_melhor_var.set(1)
      check_padrao3x1_var.set(1)
  if check_all_var.get() == 0:
      check_mhi_var.set(0)
      check_mhi2_var.set(0)
      check_mhi3_var.set(0)
      check_mhimai_var.set(0)
      check_mhi2mai_var.set(0)
      check_mhi3mai_var.set(0)
      check_milhaomin_var.set(0)
      check_milhaomax_var.set(0)
      check_torres_var.set(0)
      check_padrao23_var.set(0)
      check_melhor_var.set(0)
      check_padrao3x1_var.set(0)
    
check_all = Checkbutton(bg = color_fondo,activebackground = color_fondo, variable = check_all_var, command =lambda:[app.after(30,seleccionar_todo), app.after(30,seleted_estrategias)])
check_all.place(x=85, y=341+20)

############################################BOTONES TOP#####################################################################

    
btn_ver_assets = Button(borderwidth = 0, image = btn_assets_foto, bg = "white", command=lambda:[app.after(200,status_assets_start)])                                                                                      
btn_ver_assets.place(x=200, y=24)
 
 
def enviar_profit_p1():
    global profit_all
    global divisa
    global profit1
    selected = combo_par_p5.get()
    indice = divisa.index(selected)    
    profit1 =float((profit_all[indice]/100))
    
def enviar_profit_p2():
    global profit_all
    global divisa
    global profit2
    selected = combo_par_p5.get()
    indice = divisa.index(selected)    
    profit2 =float((profit_all[indice]/100))

def enviar_profit_p3():
    global profit_all
    global divisa
    global profit3
    selected = combo_par_p5.get()
    indice = divisa.index(selected)    
    profit3 =float((profit_all[indice]/100))

def enviar_profit_p4():
    global profit_all
    global divisa
    global profit4
    selected = combo_par_p4.get()
    indice = divisa.index(selected)    
    profit4 =float((profit_all[indice]/100))
    
def enviar_profit_p5():
    global profit_all
    global divisa
    global profit5
    selected = combo_par_p5.get()
    indice = divisa.index(selected)    
    profit5 =float((profit_all[indice]/100))  
##################################PANEL 1######################################################3
 
combo_mode_label_p1 = Label(text="REAL", fg = "spring green",bg= color_fondo)
combo_mode_label_p1.config(font=('Arial',7))
combo_mode_label_p1.place(x=163,y=92)

combo_estrategia_p1 = ttk.Combobox(app, width= 8, values=["MHI","MHI-MAI","Milhao min", "Milhao max"])
combo_estrategia_p1.grid(column=2, row=2)
combo_estrategia_p1.current(0)
combo_estrategia_p1.place(x=163,y=118)
   
combo_par_p1 = ttk.Combobox(app, width= 8, values=divisa)
combo_par_p1.grid(column=2, row=2)
combo_par_p1.current(0)
combo_par_p1.place(x=163,y=144) 
combo_par_p1.bind("<<ComboboxSelected>>", enviar_profit_p1)

ingreso_p1 = Entry(width=5)
ingreso_p1.insert(0, "1")
ingreso_p1.place(x=250, y=170)

combo_entrada_p1 = ttk.Combobox(app, width= 1, values=["1", "2", "3", "4", "5"])
combo_entrada_p1.grid(column=2, row=2)
combo_entrada_p1.current(2)
combo_entrada_p1.place(x=163,y=170)

mg_text_p1 = Entry(width=5)
mg_text_p1.insert(0, "0")
mg_text_p1.place(x=250, y=196)

combo_mgmodo_p1 = ttk.Combobox(app, width= 1, values=["0", "1"])
combo_mgmodo_p1.grid(column=2, row=2)
combo_mgmodo_p1.current(0)
combo_mgmodo_p1.place(x=163,y=196)

stop_gain_p1 = Entry(width=4)
stop_gain_p1.insert(0, "0")
stop_gain_p1.place(x=163, y=222)

stop_loss_p1 = Entry(width=5)
stop_loss_p1.insert(0, "0")
stop_loss_p1.place(x=250, y=222)

limite_hora_p1 = Entry(width=4)
limite_hora_p1.insert(0, "0")
limite_hora_p1.place(x=163, y=248)

limite_minuto_p1 = Entry(width=5)
limite_minuto_p1.insert(0, "0")
limite_minuto_p1.place(x=250, y=248)
 
start_panel1 = Button(borderwidth = 0, image=start, bg = color_fondo2, command=lambda:[app.after(200,enviar_profit_p1),app.after(200,antesala_panel1,combo_estrategia_p1.get(),ingreso_p1.get(),combo_par_p1.get(), combo_entrada_p1.get(),combo_mgmodo_p1.get(),mg_text_p1.get(),stop_gain_p1.get(),stop_loss_p1.get(),limite_hora_p1.get(),limite_minuto_p1.get(),check_lowest_var.get(),check_low_var.get(),check_normal_var.get(),check_high_var.get(),check_highest_var.get()),app.after(200,boton_on_off_p1,0),app.after(200,start_score_p1),app.after(200,bloquiar_entrada(combo_entrada_p1.get()))])
start_panel1.place(x=243, y=109)  
 
stop_panel1 = Button(borderwidth = 0, image=stop, bg = color_fondo2, command=lambda:[app.after(200,antesala_panel1_stop,"stop"),app.after(200,boton_on_off_p1,1),app.after(200,reset_entrada)])
stop_panel1.place(x=243, y=139)   


##################################PANEL 2######################################################3
 
combo_mode_label_p2 = Label(text="REAL", fg = "spring green",bg= color_fondo)
combo_mode_label_p2.config(font=('Arial',7))
combo_mode_label_p2.place(x=163+209,y=92)

combo_estrategia_p2 = ttk.Combobox(app, width= 8, values=["MHI2","MHI2-MAI","Padrao 23"])
combo_estrategia_p2.grid(column=2, row=2)
combo_estrategia_p2.current(0)
combo_estrategia_p2.place(x=163+209,y=118)
   
combo_par_p2 = ttk.Combobox(app, width= 8, values=divisa)
combo_par_p2.grid(column=2, row=2)
combo_par_p2.current(0)
combo_par_p2.place(x=163+209,y=144) 


ingreso_p2 = Entry(width=5)
ingreso_p2.insert(0, "1")
ingreso_p2.place(x=250+209, y=170)

combo_entrada_p2 = ttk.Combobox(app, width= 1, values=["1", "2", "3", "4", "5"])
combo_entrada_p2.grid(column=2, row=2)
combo_entrada_p2.current(2)
combo_entrada_p2.place(x=163+209,y=170)

mg_text_p2 = Entry(width=5)
mg_text_p2.insert(0, "0")
mg_text_p2.place(x=250+209, y=196)

combo_mgmodo_p2 = ttk.Combobox(app, width= 1, values=["0", "1"])
combo_mgmodo_p2.grid(column=2, row=2)
combo_mgmodo_p2.current(0)
combo_mgmodo_p2.place(x=163+209,y=196)

stop_gain_p2 = Entry(width=4)
stop_gain_p2.insert(0, "0")
stop_gain_p2.place(x=163+209, y=222)

stop_loss_p2 = Entry(width=5)
stop_loss_p2.insert(0, "0")
stop_loss_p2.place(x=250+209, y=222)

limite_hora_p2 = Entry(width=4)
limite_hora_p2.insert(0, "0")
limite_hora_p2.place(x=163+209, y=248)

limite_minuto_p2 = Entry(width=5)
limite_minuto_p2.insert(0, "0")
limite_minuto_p2.place(x=250+209, y=248)
 
start_panel2 = Button(borderwidth = 0, image=start, bg = color_fondo2, command=lambda:[app.after(200,enviar_profit_p2),app.after(200,antesala_panel2,combo_estrategia_p2.get(),ingreso_p2.get(),combo_par_p2.get(), combo_entrada_p2.get(),combo_mgmodo_p2.get(),mg_text_p2.get(),stop_gain_p2.get(),stop_loss_p2.get(),limite_hora_p2.get(),limite_minuto_p2.get(),check_lowest_var.get(),check_low_var.get(),check_normal_var.get(),check_high_var.get(),check_highest_var.get()),app.after(200,boton_on_off_p2,0),app.after(200,start_score_p2),app.after(200,bloquiar_entrada(combo_entrada_p2.get()))])
start_panel2.place(x=243+209, y=109)  
 
stop_panel2 = Button(borderwidth = 0, image=stop, bg = color_fondo2, command=lambda:[app.after(200,antesala_panel2_stop,"stop"),app.after(200,boton_on_off_p2,1),app.after(200,reset_entrada)])
stop_panel2.place(x=243+209, y=139) 

##################################PANEL 3######################################################3
 
combo_mode_label_p3 = Label(text="REAL", fg = "spring green",bg= color_fondo)
combo_mode_label_p3.config(font=('Arial',7))
combo_mode_label_p3.place(x=163+418,y=92)

combo_estrategia_p3 = ttk.Combobox(app, width= 8, values=["MHI3","MHI3-MAI","Melhor 3"])
combo_estrategia_p3.grid(column=2, row=2)
combo_estrategia_p3.current(0)
combo_estrategia_p3.place(x=163+418,y=118)
   
combo_par_p3 = ttk.Combobox(app, width= 8, values=divisa)
combo_par_p3.grid(column=2, row=2)
combo_par_p3.current(0)
combo_par_p3.place(x=163+418,y=144) 


ingreso_p3 = Entry(width=5)
ingreso_p3.insert(0, "1")
ingreso_p3.place(x=250+418, y=170)

combo_entrada_p3 = ttk.Combobox(app, width= 1, values=["1", "2", "3", "4", "5"])
combo_entrada_p3.grid(column=2, row=2)
combo_entrada_p3.current(2)
combo_entrada_p3.place(x=163+418,y=170)

mg_text_p3 = Entry(width=5)
mg_text_p3.insert(0, "0")
mg_text_p3.place(x=250+418, y=196)

combo_mgmodo_p3 = ttk.Combobox(app, width= 1, values=["0", "1"])
combo_mgmodo_p3.grid(column=2, row=2)
combo_mgmodo_p3.current(0)
combo_mgmodo_p3.place(x=163+418,y=196)

stop_gain_p3 = Entry(width=4)
stop_gain_p3.insert(0, "0")
stop_gain_p3.place(x=163+418, y=222)

stop_loss_p3 = Entry(width=5)
stop_loss_p3.insert(0, "0")
stop_loss_p3.place(x=250+418, y=222)

limite_hora_p3 = Entry(width=4)
limite_hora_p3.insert(0, "0")
limite_hora_p3.place(x=163+418, y=248)

limite_minuto_p3 = Entry(width=5)
limite_minuto_p3.insert(0, "0")
limite_minuto_p3.place(x=250+418, y=248)
 
start_panel3 = Button(borderwidth = 0, image=start, bg = color_fondo2, command=lambda:[app.after(200,enviar_profit_p3),app.after(200,antesala_panel3,combo_estrategia_p3.get(),ingreso_p3.get(),combo_par_p3.get(), combo_entrada_p3.get(),combo_mgmodo_p3.get(),mg_text_p3.get(),stop_gain_p3.get(),stop_loss_p3.get(),limite_hora_p3.get(),limite_minuto_p3.get(),check_lowest_var.get(),check_low_var.get(),check_normal_var.get(),check_high_var.get(),check_highest_var.get()),app.after(200,boton_on_off_p3,0),app.after(200,start_score_p3),app.after(200,bloquiar_entrada(combo_entrada_p3.get()))])
start_panel3.place(x=243+418, y=109)  
 
stop_panel3 = Button(borderwidth = 0, image=stop, bg = color_fondo2, command=lambda:[app.after(200,antesala_panel3_stop,"stop"),app.after(200,boton_on_off_p3,1),app.after(200,reset_entrada)])
stop_panel3.place(x=243+418, y=139) 

##################################PANEL 4######################################################3
 
combo_mode_label_p4 = Label(text="REAL", fg = "spring green",bg= color_fondo)
combo_mode_label_p4.config(font=('Arial',7))
combo_mode_label_p4.place(x=163+627,y=92)

combo_estrategia_p4 = ttk.Combobox(app, width= 8, values=["Torres G","Padrao 3x1"])
combo_estrategia_p4.grid(column=2, row=2)
combo_estrategia_p4.current(0)
combo_estrategia_p4.place(x=163+627,y=118)
   
combo_par_p4 = ttk.Combobox(app, width= 8, values=divisa)
combo_par_p4.grid(column=2, row=2)
combo_par_p4.current(0)
combo_par_p4.place(x=163+627,y=144) 


ingreso_p4 = Entry(width=5)
ingreso_p4.insert(0, "1")
ingreso_p4.place(x=250+627, y=170)

combo_entrada_p4 = ttk.Combobox(app, width= 1, values=["1", "2", "3", "4", "5"])
combo_entrada_p4.grid(column=2, row=2)
combo_entrada_p4.current(2)
combo_entrada_p4.place(x=163+627,y=170)

mg_text_p4 = Entry(width=5)
mg_text_p4.insert(0, "0")
mg_text_p4.place(x=250+627, y=196)

combo_mgmodo_p4 = ttk.Combobox(app, width= 1, values=["0", "1"])
combo_mgmodo_p4.grid(column=2, row=2)
combo_mgmodo_p4.current(0)
combo_mgmodo_p4.place(x=163+627,y=196)

stop_gain_p4 = Entry(width=4)
stop_gain_p4.insert(0, "0")
stop_gain_p4.place(x=163+627, y=222)

stop_loss_p4 = Entry(width=5)
stop_loss_p4.insert(0, "0")
stop_loss_p4.place(x=250+627, y=222)

limite_hora_p4 = Entry(width=4)
limite_hora_p4.insert(0, "0")
limite_hora_p4.place(x=163+627, y=248)

limite_minuto_p4 = Entry(width=5)
limite_minuto_p4.insert(0, "0")
limite_minuto_p4.place(x=250+627, y=248)
 
start_panel4 = Button(borderwidth = 0, image=start, bg = color_fondo2, command=lambda:[app.after(200,enviar_profit_p4),app.after(200,antesala_panel4,combo_estrategia_p4.get(),ingreso_p4.get(),combo_par_p4.get(), combo_entrada_p4.get(),combo_mgmodo_p4.get(),mg_text_p4.get(),stop_gain_p4.get(),stop_loss_p4.get(),limite_hora_p4.get(),limite_minuto_p4.get(),check_lowest_var.get(),check_low_var.get(),check_normal_var.get(),check_high_var.get(),check_highest_var.get()),app.after(200,boton_on_off_p4,0),app.after(200,start_score_p4),app.after(200,bloquiar_entrada(combo_entrada_p4.get()))])
start_panel4.place(x=243+627, y=109)  
 
stop_panel4 = Button(borderwidth = 0, image=stop, bg = color_fondo2, command=lambda:[app.after(200,antesala_panel4_stop,"stop"),app.after(200,boton_on_off_p4,1),app.after(200,reset_entrada)])
stop_panel4.place(x=243+627, y=139)

#######################################################PANEL 5##################################

after_loss_p5 = ttk.Combobox(app, width= 1, values=["0","1", "2", "3"],state="readonly")
after_loss_p5.grid(column=2, row=2)
after_loss_p5.current(0)
after_loss_p5.place(x=163+820,y=144)

martingala_af_p5 = ttk.Combobox(app, width= 1, values=["0","1","2","3","4"],state="readonly")
martingala_af_p5.grid(column=2, row=2)
martingala_af_p5.current(0)
martingala_af_p5.place(x=163+837+36,y=144)

num_ops_p5 = Entry(width=4)
num_ops_p5.insert(0, "1")
num_ops_p5.place(x=250+843,y=144)
   
combo_par_p5 = ttk.Combobox(app, width= 7, values=divisa,state="readonly")
combo_par_p5.grid(column=2, row=2)
combo_par_p5.current(0)
combo_par_p5.place(x=163+820,y=117) 

modo_entrada_p5 = ttk.Combobox(app, width= 1, values=["1", "2", "3","4","5"],state="readonly")
modo_entrada_p5.grid(column=2, row=2)
modo_entrada_p5.current(0)
modo_entrada_p5.place(x=163+837,y=170)

ingreso_p5 = Entry(width=5)
ingreso_p5.insert(0, "1")
ingreso_p5.place(x=250+837,y=170)

mg_text_p5 = Entry(width=5)
mg_text_p5.insert(0, "0")
mg_text_p5.place(x=250+837, y=196)

combo_mgmodo_p5 = ttk.Combobox(app, width= 1, values=["0", "1", "2"],state="readonly")
combo_mgmodo_p5.grid(column=2, row=2)
combo_mgmodo_p5.current(0)
combo_mgmodo_p5.place(x=163+837,y=196)

stop_gain_p5 = Entry(width=4)
stop_gain_p5.insert(0, "0")
stop_gain_p5.place(x=163+837, y=222)

stop_loss_p5 = Entry(width=5)
stop_loss_p5.insert(0, "0")
stop_loss_p5.place(x=250+837, y=222)

limite_hora_p5 = Entry(width=3)
limite_hora_p5.insert(0, "hs")
limite_hora_p5.place(x=163+817, y=248)

limite_minuto_p5 = Entry(width=3)
limite_minuto_p5.insert(0, "ms")
limite_minuto_p5.place(x=163+843, y=248)

stop_ops_p5 = Entry(width=5)
stop_ops_p5.insert(0, "0")
stop_ops_p5.place(x=250+837, y=248)
 
start_panel5 = Button(borderwidth = 0, image=start2, bg = color_fondo3, command=lambda:[app.after(200,antesala_panel5,ingreso_p5.get(),combo_par_p5.get(),after_loss_p5.get(),combo_mgmodo_p5.get(),mg_text_p5.get(),martingala_af_p5.get(),num_ops_p5.get(),modo_entrada_p5.get(),stop_gain_p5.get(),stop_loss_p5.get(),limite_hora_p5.get(),limite_minuto_p5.get(),stop_ops_p5.get(),check_mhi_var.get(),check_mhi2_var.get(),check_mhi3_var.get(),check_mhimai_var.get(),check_mhi2mai_var.get(),check_mhi3mai_var.get(),check_milhaomin_var.get(),check_milhaomax_var.get(),check_torres_var.get(),check_padrao23_var.get(),check_melhor_var.get(),check_padrao3x1_var.get(),check_lowest_var.get(),check_low_var.get(),check_normal_var.get(),check_high_var.get(),check_highest_var.get()), app.after(200,boton_on_off_p5,0),app.after(200,start_score_p5)])
start_panel5.place(x=243+807, y=112)
start_panel5.config(state="disabled")
   
stop_panel5 = Button(borderwidth = 0, image=stop2, bg = color_fondo3, command=lambda:[app.after(200,antesala_panel5_stop,"stop"),app.after(200,boton_on_off_p5,1)])
stop_panel5.place(x=243+844, y=112)

def bloquiar_entrada(entrada_recibida):
    
    combo_entrada_p1['values'] = entrada_recibida
    combo_entrada_p1.current(0)
    combo_entrada_p2['values'] = entrada_recibida
    combo_entrada_p2.current(0)
    combo_entrada_p3['values'] = entrada_recibida
    combo_entrada_p3.current(0)
    combo_entrada_p4['values'] = entrada_recibida
    combo_entrada_p4.current(0)
    
def reset_entrada():
    global on_p1
    global on_p2
    global on_p3
    global on_p4
    
    if on_p1 == 1 and on_p2 == 1 and on_p3 == 1 and on_p4 == 1: 
     start_panel5.config(state="normal")   
     combo_entrada_p1['values'] = ["1","2","3","4","5"]
     combo_entrada_p1.current(0)
     combo_entrada_p2['values'] = ["1","2","3","4","5"]
     combo_entrada_p2.current(0)
     combo_entrada_p3['values'] = ["1","2","3","4","5"]
     combo_entrada_p3.current(0)
     combo_entrada_p4['values'] = ["1","2","3","4","5"]
     combo_entrada_p4.current(0)
    
def actualizar_assets():
    global divisa
    combo_par_p1['values'] = divisa
    combo_par_p1.current(0)
    
    combo_par_p2['values'] = divisa
    combo_par_p2.current(0)
    
    combo_par_p3['values'] = divisa
    combo_par_p3.current(0)
    
    combo_par_p4['values'] = divisa
    combo_par_p4.current(0)
    
    combo_par_p5['values'] = divisa
    combo_par_p5.current(0)
    

on_panel1 = Button(borderwidth = 0, image=off, bg = color_fondo2)
on_panel1.place(x=255, y=89)
on_panel2 = Button(borderwidth = 0, image=off, bg = color_fondo2)
on_panel2.place(x=255+209, y=89)
on_panel3 = Button(borderwidth = 0, image=off, bg = color_fondo2)
on_panel3.place(x=255+418, y=89)
on_panel4 = Button(borderwidth = 0, image=off, bg = color_fondo2)
on_panel4.place(x=255+627, y=89)
on_panel5 = Button(borderwidth = 0, image=off2, bg = color_fondo3)
on_panel5.place(x=170+792, y=98)


def boton_on_off_p1(boton_modo):
  global on_p1
  on_p1 = boton_modo
  if boton_modo == 0:
   on_panel1.config(image=on)
   start_panel1.config(state="disabled")
   start_panel5.config(state="disabled")
  if boton_modo == 1:
   on_panel1.config(image=off)
   start_panel1.config(state="normal")

def boton_on_off_p2(boton_modo):
  global on_p2
  on_p2 = boton_modo
  if boton_modo == 0:
   on_panel2.config(image=on)
   start_panel2.config(state="disabled")
   start_panel5.config(state="disabled")
  if boton_modo == 1:
   on_panel2.config(image=off)
   start_panel2.config(state="normal")

def boton_on_off_p3(boton_modo): 
  global on_p3
  on_p3 = boton_modo  
  if boton_modo == 0:
   on_panel3.config(image=on)
   start_panel3.config(state="disabled")
   start_panel5.config(state="disabled")
  if boton_modo == 1:
   on_panel3.config(image=off)
   start_panel3.config(state="normal")
   
def boton_on_off_p4(boton_modo):
  global on_p4
  on_p4 = boton_modo
  if boton_modo == 0:
   on_panel4.config(image=on)
   start_panel4.config(state="disabled")
   start_panel5.config(state="disabled")
  if boton_modo == 1:
   on_panel4.config(image=off)
   start_panel4.config(state="normal")

def boton_on_off_p5(boton_modo):
  if boton_modo == 0:
   on_panel5.config(image=on2)
   start_panel1.config(state="disabled")
   start_panel2.config(state="disabled")
   start_panel3.config(state="disabled")
   start_panel4.config(state="disabled")
   start_panel5.config(state="disabled")
  if boton_modo == 1:
   on_panel5.config(image=off2)
   start_panel1.config(state="normal")
   start_panel2.config(state="normal")
   start_panel3.config(state="normal")
   start_panel4.config(state="normal")
   start_panel5.config(state="normal")
      
###########################################################################BARRA DE HISTORIAL Y BALANCE########################
  

##############################DIVISAS GRAFICOS Y MAS####################################################################
combo_tipo_martin = ttk.Combobox(app, width= 7, values=["MG0","MG1", "MG2", "MG3", "MG4", "MG5"])
combo_tipo_martin.grid(column=2, row=2)
combo_tipo_martin.current(2)
combo_tipo_martin.place(x=11,y=127)

assets_1 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[0])])
assets_1.place(x=4, y=156)
assets_1_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_1_label_profit.config(font=('Arial',8))
assets_1_label_profit.place(x=43, y=161)
assets_1_label = Label(text="", fg = "white",bg= color_fondo)
assets_1_label.config(font=('Arial',5))
assets_1_label.place(x=42, y=178)


assets_2 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[1])])
assets_2.place(x=4, y=156+40)
assets_2_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_2_label_profit.config(font=('Arial',8))
assets_2_label_profit.place(x=43, y=161+40)
assets_2_label = Label(text="", fg = "white",bg= color_fondo)
assets_2_label.config(font=('Arial',5))
assets_2_label.place(x=42, y=178+40)

assets_3 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[2])])
assets_3.place(x=4, y=156+80)
assets_3_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_3_label_profit.config(font=('Arial',8))
assets_3_label_profit.place(x=43, y=161+80)
assets_3_label = Label(text="", fg = "white",bg= color_fondo)
assets_3_label.config(font=('Arial',5))
assets_3_label.place(x=42, y=178+80)


assets_4 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[3])])
assets_4.place(x=4, y=156+120)
assets_4_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_4_label_profit.config(font=('Arial',8))
assets_4_label_profit.place(x=43, y=161+120)
assets_4_label = Label(text="", fg = "white",bg= color_fondo)
assets_4_label.config(font=('Arial',5))
assets_4_label.place(x=42, y=178+120)


assets_5 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[4])])
assets_5.place(x=4, y=156+160)
assets_5_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_5_label_profit.config(font=('Arial',8))
assets_5_label_profit.place(x=43, y=161+160)
assets_5_label = Label(text="", fg = "white",bg= color_fondo)
assets_5_label.config(font=('Arial',5))
assets_5_label.place(x=42, y=178+160)

assets_6 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[5])])
assets_6.place(x=4, y=156+200)
assets_6_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_6_label_profit.config(font=('Arial',8))
assets_6_label_profit.place(x=43, y=161+200)
assets_6_label = Label(text="", fg = "white",bg= color_fondo)
assets_6_label.config(font=('Arial',5))
assets_6_label.place(x=42, y=178+200)

assets_7 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[6])])
assets_7.place(x=4, y=156+240)
assets_7_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_7_label_profit.config(font=('Arial',8))
assets_7_label_profit.place(x=43, y=161+240)
assets_7_label = Label(text="", fg = "white",bg= color_fondo)
assets_7_label.config(font=('Arial',5))
assets_7_label.place(x=42, y=178+240)

assets_8 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[7])])
assets_8.place(x=4, y=156+280)
assets_8_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_8_label_profit.config(font=('Arial',8))
assets_8_label_profit.place(x=43, y=161+280)
assets_8_label = Label(text="", fg = "white",bg= color_fondo)
assets_8_label.config(font=('Arial',5))
assets_8_label.place(x=42, y=178+280)

assets_9 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[8])])
assets_9.place(x=4, y=156+320)
assets_9_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_9_label_profit.config(font=('Arial',8))
assets_9_label_profit.place(x=43, y=161+320)
assets_9_label = Label(text="", fg = "white",bg= color_fondo)
assets_9_label.config(font=('Arial',5))
assets_9_label.place(x=42, y=178+320)

assets_10 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[9])])
assets_10.place(x=4, y=156+360)
assets_10_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_10_label_profit.config(font=('Arial',8))
assets_10_label_profit.place(x=43, y=161+360)
assets_10_label = Label(text="", fg = "white",bg= color_fondo)
assets_10_label.config(font=('Arial',5))
assets_10_label.place(x=42, y=178+360)

assets_11 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[10])])
assets_11.place(x=4, y=156+400)
assets_11_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_11_label_profit.config(font=('Arial',8))
assets_11_label_profit.place(x=43, y=161+400)
assets_11_label = Label(text="", fg = "white",bg= color_fondo)
assets_11_label.config(font=('Arial',5))
assets_11_label.place(x=42, y=178+400)

assets_12 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[11])])
assets_12.place(x=4, y=156+440)
assets_12_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_12_label_profit.config(font=('Arial',8))
assets_12_label_profit.place(x=43, y=161+440)
assets_12_label = Label(text="", fg = "white",bg= color_fondo)
assets_12_label.config(font=('Arial',5))
assets_12_label.place(x=42, y=178+440)

assets_13 = Button(borderwidth = 0.0, bg= color_fondo, command=lambda:[app.after(500,llamar_velas,combo_tipo_martin.get(),divisa[12])])
assets_13.place(x=4, y=156+480)
assets_13_label_profit = Label(text="", fg = "spring green",bg= color_fondo)
assets_13_label_profit.config(font=('Arial',8))
assets_13_label_profit.place(x=43, y=161+480)
assets_13_label = Label(text="", fg = "white",bg= color_fondo)
assets_13_label.config(font=('Arial',5))
assets_13_label.place(x=42, y=178+480)

def graf_assets(descripcion,comision,nombre):
   assets_1.config(bg= color_fondo) 
   assets_1_label_profit.config(bg= color_fondo)
   assets_1_label.config(bg= color_fondo) 
   assets_2.config(bg= color_fondo) 
   assets_2_label_profit.config(bg= color_fondo)
   assets_2_label.config(bg= color_fondo)
   assets_3.config(bg= color_fondo) 
   assets_3_label_profit.config(bg= color_fondo)
   assets_3_label.config(bg= color_fondo)
   assets_4.config(bg= color_fondo) 
   assets_4_label_profit.config(bg= color_fondo)
   assets_4_label.config(bg= color_fondo)
   assets_5.config(bg= color_fondo) 
   assets_5_label_profit.config(bg= color_fondo)
   assets_5_label.config(bg= color_fondo)
   assets_6.config(bg= color_fondo) 
   assets_6_label_profit.config(bg= color_fondo)
   assets_6_label.config(bg= color_fondo)
   assets_7.config(bg= color_fondo) 
   assets_7_label_profit.config(bg= color_fondo)
   assets_7_label.config(bg= color_fondo)
   assets_8.config(bg= color_fondo) 
   assets_8_label_profit.config(bg= color_fondo)
   assets_8_label.config(bg= color_fondo)
   assets_9.config(bg= color_fondo) 
   assets_9_label_profit.config(bg= color_fondo)
   assets_9_label.config(bg= color_fondo)
   assets_10.config(bg= color_fondo) 
   assets_10_label_profit.config(bg= color_fondo)
   assets_10_label.config(bg= color_fondo)
   assets_11.config(bg= color_fondo) 
   assets_11_label_profit.config(bg= color_fondo)
   assets_11_label.config(bg= color_fondo)
   assets_12.config(bg= color_fondo) 
   assets_12_label_profit.config(bg= color_fondo)
   assets_12_label.config(bg= color_fondo)
   assets_13.config(bg= color_fondo) 
   assets_13_label_profit.config(bg= color_fondo)
   assets_13_label.config(bg= color_fondo)
   global divisa
   global profit_all
   profit_all = comision
   divisa = nombre
   actualizar_assets()
   cuenta = len(descripcion)
   if cuenta >= 1:
       assets_1.config(image = seleccionar_foto(nombre[0]))
       profit2 = 100 - comision[0] 
       profit=str(profit2)
       assets_1_label_profit.config(text="+"+profit+"%")
       assets_1_label.config(text=descripcion[0])
   
   if cuenta >= 2:
       assets_2.config(image = seleccionar_foto(nombre[1]))
       profit2 = 100 - comision[1] 
       profit=str(profit2)
       assets_2_label_profit.config(text="+"+profit+"%")
       assets_2_label.config(text=descripcion[1])
    
   if cuenta >= 3:
       assets_3.config(image = seleccionar_foto(nombre[2]))
       profit2 = 100 - comision[2] 
       profit=str(profit2)
       assets_3_label_profit.config(text="+"+profit+"%")
       assets_3_label.config(text=descripcion[2])
   
   if cuenta >= 4:
       assets_4.config(image = seleccionar_foto(nombre[3]))
       profit2 = 100 - comision[3] 
       profit=str(profit2)
       assets_4_label_profit.config(text="+"+profit+"%")
       assets_4_label.config(text=descripcion[3])
 
   if cuenta >= 5:
       assets_5.config(image = seleccionar_foto(nombre[4]))
       profit2 = 100 - comision[4] 
       profit=str(profit2)
       assets_5_label_profit.config(text="+"+profit+"%")
       assets_5_label.config(text=descripcion[4])
   
   if cuenta >= 6:
       assets_6.config(image = seleccionar_foto(nombre[5]))
       profit2 = 100 - comision[5] 
       profit=str(profit2)
       assets_6_label_profit.config(text="+"+profit+"%")
       assets_6_label.config(text=descripcion[5])
    
   if cuenta >= 7:
       assets_7.config(image = seleccionar_foto(nombre[6]))
       profit2 = 100 - comision[6] 
       profit=str(profit2)
       assets_7_label_profit.config(text="+"+profit+"%")
       assets_7_label.config(text=descripcion[6])
   
   if cuenta >= 8:
       assets_8.config(image = seleccionar_foto(nombre[7]))
       profit2 = 100 - comision[7] 
       profit=str(profit2)
       assets_8_label_profit.config(text="+"+profit+"%")
       assets_8_label.config(text=descripcion[7])
       
   if cuenta >= 9:
       assets_9.config(image = seleccionar_foto(nombre[8]))
       profit2 = 100 - comision[8] 
       profit=str(profit2)
       assets_9_label_profit.config(text="+"+profit+"%")
       assets_9_label.config(text=descripcion[8])
    
   if cuenta >= 10:
       assets_10.config(image = seleccionar_foto(nombre[9]))
       profit2 = 100 - comision[9] 
       profit=str(profit2)
       assets_10_label_profit.config(text="+"+profit+"%")
       assets_10_label.config(text=descripcion[9])
   
   if cuenta >= 11:
       assets_11.config(image = seleccionar_foto(nombre[10]))
       profit2 = 100 - comision[10] 
       profit=str(profit2)
       assets_11_label_profit.config(text="+"+profit+"%")
       assets_11_label.config(text=descripcion[10])
    
   if cuenta >= 12:
       assets_12.config(image = seleccionar_foto(nombre[11]))
       profit2 = 100 - comision[11] 
       profit=str(profit2)
       assets_12_label_profit.config(text="+"+profit+"%")
       assets_12_label.config(text=descripcion[11])
   
   if cuenta >= 13:
       assets_13.config(image = seleccionar_foto(nombre[12]))
       profit2 = 100 - comision[12] 
       profit=str(profit2)
       assets_13_label_profit.config(text="+"+profit+"%")
       assets_13_label.config(text=descripcion[12])

def seleccionar_foto(seleccion):
 asset_foto = default_foto

 if seleccion == "EURUSD": asset_foto =  eurusd_foto
 if seleccion == "AUDCAD": asset_foto =  audcad_foto
 if seleccion == "AUDJPY": asset_foto =  audjpy_foto
 if seleccion == "GBPUSD": asset_foto =  gbpusd_foto
 if seleccion == "EURGBP": asset_foto =  eurgbp_foto
 if seleccion == "USDJPY": asset_foto =  usdjpy_foto
 if seleccion == "AUDUSD": asset_foto =  audusd_foto
 if seleccion == "GBPJPY": asset_foto =  gbpjpy_foto
 if seleccion == "EURJPY": asset_foto =  eurjpy_foto
 if seleccion == "BTCUSD": asset_foto =  btcusd_foto
 if seleccion == "XRPUSD": asset_foto =  xrpusd_foto
 if seleccion == "ETHUSD": asset_foto =  ethusd_foto
 if seleccion == "NZDUSD-OTC": asset_foto =  nzdusd_otc_foto
 if seleccion == "AUDCAD-OTC": asset_foto =  audcad_otc_foto
 if seleccion == "EURUSD-OTC": asset_foto =  eurusd_otc_foto
 if seleccion == "USDINR-OTC": asset_foto =  usdinr_otc_foto
 if seleccion == "USDZAR-OTC": asset_foto =  usdzar_otc_foto
 if seleccion == "USDHKD-OTC": asset_foto =  usdhkd_otc_foto
 if seleccion == "USDCHF-OTC": asset_foto =  usdchf_otc_foto
 if seleccion == "USDSGD-OTC": asset_foto =  usdsgd_otc_foto
 if seleccion == "EURGBP-OTC": asset_foto =  eurgbp_otc_foto
 if seleccion == "USDSGD-OTC": asset_foto =  usdsgd_otc_foto
 if seleccion == "GBPUSD-OTC": asset_foto =  gbpusd_otc_foto
 if seleccion == "EURJPY-OTC": asset_foto =  eurjpy_otc_foto
 return asset_foto

#############################################################IMAGENES DIVISAS GLOBALES
btn_cata_img1 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img1.place(x=115, y=319)
btn_cata_img2 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img2.place(x=325, y=319)
btn_cata_img3 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img3.place(x=535, y=319)
btn_cata_img4 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img4.place(x=745, y=319)
btn_cata_img5 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img5.place(x=955, y=319)
btn_cata_img6 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img6.place(x=1165, y=319)
btn_cata_img7 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img7.place(x=115, y=499)
btn_cata_img8 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img8.place(x=325, y=499)
btn_cata_img9 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img9.place(x=535, y=499)
btn_cata_img10 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img10.place(x=745, y=499)
btn_cata_img11= Button(borderwidth = 0, bg = color_fondo)
btn_cata_img11.place(x=955, y=499)
btn_cata_img12 = Button(borderwidth = 0, bg = color_fondo)
btn_cata_img12.place(x=1165, y=499)


    
#############################CATALOGOS GRAFICOS#########################################################################

#_____________________________CATALOGO 1___________________________________________________________________
btn_mhi_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_0.place(x=108, y=367)

btn_mhi_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_1.place(x=108+23, y=367)

btn_mhi_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_2.place(x=108+46, y=367)

btn_mhi_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_3.place(x=108+69, y=367)

btn_mhi_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_4.place(x=108+92, y=367)

btn_mhi_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_5.place(x=108+115, y=367)

btn_mhi_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_6.place(x=108+138, y=367)

btn_mhi_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_7.place(x=108+161, y=367)

btn_mhi_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_8.place(x=108, y=367+25)

btn_mhi_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_9.place(x=108+23, y=367+25)

btn_mhi_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_10.place(x=108+46, y=367+25)

btn_mhi_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_11.place(x=108+69, y=367+25)

btn_mhi_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_12.place(x=108+92, y=367+25)

btn_mhi_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_13.place(x=108+115, y=367+25)

btn_mhi_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_14.place(x=108+138, y=367+25)

btn_mhi_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_15.place(x=108+161, y=367+25)

btn_mhi_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_16.place(x=108, y=367+50)

btn_mhi_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_17.place(x=108+23, y=367+50)

btn_mhi_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_18.place(x=108+46, y=367+50)

btn_mhi_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_19.place(x=108+69, y=367+50)

btn_mhi_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_20.place(x=108+92, y=367+50)

btn_mhi_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_21.place(x=108+115, y=367+50)

btn_mhi_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_22.place(x=108+138, y=367+50)

btn_mhi_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_23.place(x=108+161, y=367+50)

btn_mhi_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_24.place(x=108, y=367+75)

btn_mhi_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_25.place(x=108+23, y=367+75)

btn_mhi_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_26.place(x=108+46, y=367+75)

btn_mhi_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_27.place(x=108+69, y=367+75)

btn_mhi_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_28.place(x=108+92, y=367+75)

btn_mhi_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_29.place(x=108+115, y=367+75)

btn_mhi_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_30.place(x=108+138, y=367+75)

btn_mhi_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_31.place(x=108+161, y=367+75)

btn_mhi_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_32.place(x=108, y=367+100)

btn_mhi_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_33.place(x=108+23, y=367+100)

btn_mhi_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_34.place(x=108+46, y=367+100)

btn_mhi_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_35.place(x=108+69, y=367+100)

btn_mhi_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_36.place(x=108+92, y=367+100)

btn_mhi_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_37.place(x=108+115, y=367+100)

btn_mhi_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_38.place(x=108+138, y=367+100)

btn_mhi_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_39.place(x=108+161, y=367+100)

lbl_porciento1 = Label(bg = color_fondo)
lbl_porciento1.place(x=108+116, y=318)
lbl_porciento1.config(font=('Arial',14))

lbl_cata_divisa1 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa1.place(x=108+44, y=330)
lbl_cata_divisa1.config(font=('Arial',7))

#_____________________________CATALOGO 2___________________________________________________________________
btn_mhi2_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_0.place(x=318, y=367)

btn_mhi2_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_1.place(x=318+23, y=367)

btn_mhi2_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_2.place(x=318+46, y=367)

btn_mhi2_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_3.place(x=318+69, y=367)

btn_mhi2_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_4.place(x=318+92, y=367)

btn_mhi2_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_5.place(x=318+115, y=367)

btn_mhi2_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_6.place(x=318+138, y=367)

btn_mhi2_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_7.place(x=318+161, y=367)

btn_mhi2_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_8.place(x=318, y=367+25)

btn_mhi2_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_9.place(x=318+23, y=367+25)

btn_mhi2_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_10.place(x=318+46, y=367+25)

btn_mhi2_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_11.place(x=318+69, y=367+25)

btn_mhi2_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_12.place(x=318+92, y=367+25)

btn_mhi2_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_13.place(x=318+115, y=367+25)

btn_mhi2_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_14.place(x=318+138, y=367+25)

btn_mhi2_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_15.place(x=318+161, y=367+25)

btn_mhi2_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_16.place(x=318, y=367+50)

btn_mhi2_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_17.place(x=318+23, y=367+50)

btn_mhi2_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_18.place(x=318+46, y=367+50)

btn_mhi2_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_19.place(x=318+69, y=367+50)

btn_mhi2_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_20.place(x=318+92, y=367+50)

btn_mhi2_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_21.place(x=318+115, y=367+50)

btn_mhi2_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_22.place(x=318+138, y=367+50)

btn_mhi2_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_23.place(x=318+161, y=367+50)

btn_mhi2_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_24.place(x=318, y=367+75)

btn_mhi2_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_25.place(x=318+23, y=367+75)

btn_mhi2_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_26.place(x=318+46, y=367+75)

btn_mhi2_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_27.place(x=318+69, y=367+75)

btn_mhi2_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_28.place(x=318+92, y=367+75)

btn_mhi2_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_29.place(x=318+115, y=367+75)

btn_mhi2_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_30.place(x=318+138, y=367+75)

btn_mhi2_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_31.place(x=318+161, y=367+75)

btn_mhi2_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_32.place(x=318, y=367+100)

btn_mhi2_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_33.place(x=318+23, y=367+100)

btn_mhi2_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_34.place(x=318+46, y=367+100)

btn_mhi2_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_35.place(x=318+69, y=367+100)

btn_mhi2_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_36.place(x=318+92, y=367+100)

btn_mhi2_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_37.place(x=318+115, y=367+100)

btn_mhi2_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_38.place(x=318+138, y=367+100)

btn_mhi2_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_39.place(x=318+161, y=367+100)

lbl_porciento2 = Label(bg = color_fondo)
lbl_porciento2.place(x=318+116, y=318)
lbl_porciento2.config(font=('Arial',14))

lbl_cata_divisa2 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa2.place(x=318+44, y=330)
lbl_cata_divisa2.config(font=('Arial',7))

#_____________________________CATALOGO 3___________________________________________________________________
btn_mhi3_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_0.place(x=528, y=367)

btn_mhi3_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_1.place(x=528+23, y=367)

btn_mhi3_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_2.place(x=528+46, y=367)

btn_mhi3_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_3.place(x=528+69, y=367)

btn_mhi3_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_4.place(x=528+92, y=367)

btn_mhi3_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_5.place(x=528+115, y=367)

btn_mhi3_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_6.place(x=528+138, y=367)

btn_mhi3_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_7.place(x=528+161, y=367)

btn_mhi3_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_8.place(x=528, y=367+25)

btn_mhi3_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_9.place(x=528+23, y=367+25)

btn_mhi3_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_10.place(x=528+46, y=367+25)

btn_mhi3_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_11.place(x=528+69, y=367+25)

btn_mhi3_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_12.place(x=528+92, y=367+25)

btn_mhi3_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_13.place(x=528+115, y=367+25)

btn_mhi3_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_14.place(x=528+138, y=367+25)

btn_mhi3_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_15.place(x=528+161, y=367+25)

btn_mhi3_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_16.place(x=528, y=367+50)

btn_mhi3_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_17.place(x=528+23, y=367+50)

btn_mhi3_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_18.place(x=528+46, y=367+50)

btn_mhi3_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_19.place(x=528+69, y=367+50)

btn_mhi3_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_20.place(x=528+92, y=367+50)

btn_mhi3_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_21.place(x=528+115, y=367+50)

btn_mhi3_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_22.place(x=528+138, y=367+50)

btn_mhi3_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_23.place(x=528+161, y=367+50)

btn_mhi3_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_24.place(x=528, y=367+75)

btn_mhi3_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_25.place(x=528+23, y=367+75)

btn_mhi3_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_26.place(x=528+46, y=367+75)

btn_mhi3_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_27.place(x=528+69, y=367+75)

btn_mhi3_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_28.place(x=528+92, y=367+75)

btn_mhi3_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_29.place(x=528+115, y=367+75)

btn_mhi3_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_30.place(x=528+138, y=367+75)

btn_mhi3_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_31.place(x=528+161, y=367+75)

btn_mhi3_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_32.place(x=528, y=367+100)

btn_mhi3_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_33.place(x=528+23, y=367+100)

btn_mhi3_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_34.place(x=528+46, y=367+100)

btn_mhi3_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_35.place(x=528+69, y=367+100)

btn_mhi3_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_36.place(x=528+92, y=367+100)

btn_mhi3_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_37.place(x=528+115, y=367+100)

btn_mhi3_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_38.place(x=528+138, y=367+100)

btn_mhi3_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_39.place(x=528+161, y=367+100)

lbl_porciento3 = Label(bg = color_fondo)
lbl_porciento3.place(x=528+116, y=318)
lbl_porciento3.config(font=('Arial',14))

lbl_cata_divisa3 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa3.place(x=528+44, y=330)
lbl_cata_divisa3.config(font=('Arial',7))



#_____________________________CATALOGO 4___________________________________________________________________
btn_mhi_mai_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_0.place(x=738, y=367)

btn_mhi_mai_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_1.place(x=738+23, y=367)

btn_mhi_mai_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_2.place(x=738+46, y=367)

btn_mhi_mai_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_3.place(x=738+69, y=367)

btn_mhi_mai_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_4.place(x=738+92, y=367)

btn_mhi_mai_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_5.place(x=738+115, y=367)

btn_mhi_mai_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_6.place(x=738+138, y=367)

btn_mhi_mai_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_7.place(x=738+161, y=367)

btn_mhi_mai_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_8.place(x=738, y=367+25)

btn_mhi_mai_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_9.place(x=738+23, y=367+25)

btn_mhi_mai_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_10.place(x=738+46, y=367+25)

btn_mhi_mai_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_11.place(x=738+69, y=367+25)

btn_mhi_mai_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_12.place(x=738+92, y=367+25)

btn_mhi_mai_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_13.place(x=738+115, y=367+25)

btn_mhi_mai_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_14.place(x=738+138, y=367+25)

btn_mhi_mai_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_15.place(x=738+161, y=367+25)

btn_mhi_mai_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_16.place(x=738, y=367+50)

btn_mhi_mai_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_17.place(x=738+23, y=367+50)

btn_mhi_mai_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_18.place(x=738+46, y=367+50)

btn_mhi_mai_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_19.place(x=738+69, y=367+50)

btn_mhi_mai_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_20.place(x=738+92, y=367+50)

btn_mhi_mai_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_21.place(x=738+115, y=367+50)

btn_mhi_mai_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_22.place(x=738+138, y=367+50)

btn_mhi_mai_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_23.place(x=738+161, y=367+50)

btn_mhi_mai_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_24.place(x=738, y=367+75)

btn_mhi_mai_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_25.place(x=738+23, y=367+75)

btn_mhi_mai_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_26.place(x=738+46, y=367+75)

btn_mhi_mai_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_27.place(x=738+69, y=367+75)

btn_mhi_mai_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_28.place(x=738+92, y=367+75)

btn_mhi_mai_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_29.place(x=738+115, y=367+75)

btn_mhi_mai_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_30.place(x=738+138, y=367+75)

btn_mhi_mai_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_31.place(x=738+161, y=367+75)

btn_mhi_mai_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_32.place(x=738, y=367+100)

btn_mhi_mai_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_33.place(x=738+23, y=367+100)

btn_mhi_mai_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_34.place(x=738+46, y=367+100)

btn_mhi_mai_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_35.place(x=738+69, y=367+100)

btn_mhi_mai_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_36.place(x=738+92, y=367+100)

btn_mhi_mai_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_37.place(x=738+115, y=367+100)

btn_mhi_mai_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_38.place(x=738+138, y=367+100)

btn_mhi_mai_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi_mai_39.place(x=738+161, y=367+100)

lbl_porciento4 = Label(bg = color_fondo)
lbl_porciento4.place(x=738+116, y=318)
lbl_porciento4.config(font=('Arial',14))

lbl_cata_divisa4 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa4.place(x=738+44, y=330)
lbl_cata_divisa4.config(font=('Arial',7))

#_____________________________CATALOGO 5___________________________________________________________________
btn_mhi2_mai_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_0.place(x=948, y=367)

btn_mhi2_mai_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_1.place(x=948+23, y=367)

btn_mhi2_mai_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_2.place(x=948+46, y=367)

btn_mhi2_mai_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_3.place(x=948+69, y=367)

btn_mhi2_mai_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_4.place(x=948+92, y=367)

btn_mhi2_mai_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_5.place(x=948+115, y=367)

btn_mhi2_mai_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_6.place(x=948+138, y=367)

btn_mhi2_mai_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_7.place(x=948+161, y=367)

btn_mhi2_mai_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_8.place(x=948, y=367+25)

btn_mhi2_mai_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_9.place(x=948+23, y=367+25)

btn_mhi2_mai_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_10.place(x=948+46, y=367+25)

btn_mhi2_mai_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_11.place(x=948+69, y=367+25)

btn_mhi2_mai_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_12.place(x=948+92, y=367+25)

btn_mhi2_mai_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_13.place(x=948+115, y=367+25)

btn_mhi2_mai_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_14.place(x=948+138, y=367+25)

btn_mhi2_mai_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_15.place(x=948+161, y=367+25)

btn_mhi2_mai_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_16.place(x=948, y=367+50)

btn_mhi2_mai_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_17.place(x=948+23, y=367+50)

btn_mhi2_mai_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_18.place(x=948+46, y=367+50)

btn_mhi2_mai_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_19.place(x=948+69, y=367+50)

btn_mhi2_mai_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_20.place(x=948+92, y=367+50)

btn_mhi2_mai_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_21.place(x=948+115, y=367+50)

btn_mhi2_mai_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_22.place(x=948+138, y=367+50)

btn_mhi2_mai_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_23.place(x=948+161, y=367+50)

btn_mhi2_mai_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_24.place(x=948, y=367+75)

btn_mhi2_mai_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_25.place(x=948+23, y=367+75)

btn_mhi2_mai_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_26.place(x=948+46, y=367+75)

btn_mhi2_mai_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_27.place(x=948+69, y=367+75)

btn_mhi2_mai_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_28.place(x=948+92, y=367+75)

btn_mhi2_mai_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_29.place(x=948+115, y=367+75)

btn_mhi2_mai_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_30.place(x=948+138, y=367+75)

btn_mhi2_mai_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_31.place(x=948+161, y=367+75)

btn_mhi2_mai_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_32.place(x=948, y=367+100)

btn_mhi2_mai_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_33.place(x=948+23, y=367+100)

btn_mhi2_mai_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_34.place(x=948+46, y=367+100)

btn_mhi2_mai_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_35.place(x=948+69, y=367+100)

btn_mhi2_mai_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_36.place(x=948+92, y=367+100)

btn_mhi2_mai_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_37.place(x=948+115, y=367+100)

btn_mhi2_mai_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_38.place(x=948+138, y=367+100)

btn_mhi2_mai_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi2_mai_39.place(x=948+161, y=367+100)

lbl_porciento5 = Label(bg = color_fondo)
lbl_porciento5.place(x=948+116, y=318)
lbl_porciento5.config(font=('Arial',14))

lbl_cata_divisa5 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa5.place(x=948+44, y=330)
lbl_cata_divisa5.config(font=('Arial',7))

#_____________________________CATALOGO 6___________________________________________________________________
btn_mhi3_mai_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_0.place(x=1158, y=367)

btn_mhi3_mai_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_1.place(x=1158+23, y=367)

btn_mhi3_mai_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_2.place(x=1158+46, y=367)

btn_mhi3_mai_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_3.place(x=1158+69, y=367)

btn_mhi3_mai_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_4.place(x=1158+92, y=367)

btn_mhi3_mai_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_5.place(x=1158+115, y=367)

btn_mhi3_mai_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_6.place(x=1158+138, y=367)

btn_mhi3_mai_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_7.place(x=1158+161, y=367)

btn_mhi3_mai_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_8.place(x=1158, y=367+25)

btn_mhi3_mai_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_9.place(x=1158+23, y=367+25)

btn_mhi3_mai_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_10.place(x=1158+46, y=367+25)

btn_mhi3_mai_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_11.place(x=1158+69, y=367+25)

btn_mhi3_mai_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_12.place(x=1158+92, y=367+25)

btn_mhi3_mai_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_13.place(x=1158+115, y=367+25)

btn_mhi3_mai_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_14.place(x=1158+138, y=367+25)

btn_mhi3_mai_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_15.place(x=1158+161, y=367+25)

btn_mhi3_mai_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_16.place(x=1158, y=367+50)

btn_mhi3_mai_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_17.place(x=1158+23, y=367+50)

btn_mhi3_mai_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_18.place(x=1158+46, y=367+50)

btn_mhi3_mai_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_19.place(x=1158+69, y=367+50)

btn_mhi3_mai_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_20.place(x=1158+92, y=367+50)

btn_mhi3_mai_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_21.place(x=1158+115, y=367+50)

btn_mhi3_mai_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_22.place(x=1158+138, y=367+50)

btn_mhi3_mai_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_23.place(x=1158+161, y=367+50)

btn_mhi3_mai_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_24.place(x=1158, y=367+75)

btn_mhi3_mai_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_25.place(x=1158+23, y=367+75)

btn_mhi3_mai_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_26.place(x=1158+46, y=367+75)

btn_mhi3_mai_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_27.place(x=1158+69, y=367+75)

btn_mhi3_mai_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_28.place(x=1158+92, y=367+75)

btn_mhi3_mai_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_29.place(x=1158+115, y=367+75)

btn_mhi3_mai_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_30.place(x=1158+138, y=367+75)

btn_mhi3_mai_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_31.place(x=1158+161, y=367+75)

btn_mhi3_mai_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_32.place(x=1158, y=367+100)

btn_mhi3_mai_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_33.place(x=1158+23, y=367+100)

btn_mhi3_mai_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_34.place(x=1158+46, y=367+100)

btn_mhi3_mai_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_35.place(x=1158+69, y=367+100)

btn_mhi3_mai_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_36.place(x=1158+92, y=367+100)

btn_mhi3_mai_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_37.place(x=1158+115, y=367+100)

btn_mhi3_mai_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_38.place(x=1158+138, y=367+100)

btn_mhi3_mai_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_mhi3_mai_39.place(x=1158+161, y=367+100)

lbl_porciento6 = Label(bg = color_fondo)
lbl_porciento6.place(x=1158+116, y=318)
lbl_porciento6.config(font=('Arial',14))

lbl_cata_divisa6 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa6.place(x=1158+44, y=330)
lbl_cata_divisa6.config(font=('Arial',7))
    
#_____________________________CATALOGO 7___________________________________________________________________
milhao_min_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_0.place(x=108, y=552)

milhao_min_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_1.place(x=108+23, y=552)

milhao_min_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_2.place(x=108+46, y=552)

milhao_min_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_3.place(x=108+69, y=552)

milhao_min_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_4.place(x=108+92, y=552)

milhao_min_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_5.place(x=108+115, y=552)

milhao_min_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_6.place(x=108+138, y=552)

milhao_min_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_7.place(x=108+161, y=552)

milhao_min_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_8.place(x=108, y=552+25)

milhao_min_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_9.place(x=108+23, y=552+25)

milhao_min_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_10.place(x=108+46, y=552+25)

milhao_min_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_11.place(x=108+69, y=552+25)

milhao_min_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_12.place(x=108+92, y=552+25)

milhao_min_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_13.place(x=108+115, y=552+25)

milhao_min_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_14.place(x=108+138, y=552+25)

milhao_min_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_15.place(x=108+161, y=552+25)

milhao_min_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_16.place(x=108, y=552+50)

milhao_min_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_17.place(x=108+23, y=552+50)

milhao_min_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_18.place(x=108+46, y=552+50)

milhao_min_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_19.place(x=108+69, y=552+50)

milhao_min_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_20.place(x=108+92, y=552+50)

milhao_min_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_21.place(x=108+115, y=552+50)

milhao_min_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_22.place(x=108+138, y=552+50)

milhao_min_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_23.place(x=108+161, y=552+50)

milhao_min_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_24.place(x=108, y=552+75)

milhao_min_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_25.place(x=108+23, y=552+75)

milhao_min_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_26.place(x=108+46, y=552+75)

milhao_min_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_27.place(x=108+69, y=552+75)

milhao_min_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_28.place(x=108+92, y=552+75)

milhao_min_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_29.place(x=108+115, y=552+75)

milhao_min_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_30.place(x=108+138, y=552+75)

milhao_min_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_31.place(x=108+161, y=552+75)

milhao_min_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_32.place(x=108, y=552+100)

milhao_min_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_33.place(x=108+23, y=552+100)

milhao_min_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_34.place(x=108+46, y=552+100)

milhao_min_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_35.place(x=108+69, y=552+100)

milhao_min_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_36.place(x=108+92, y=552+100)

milhao_min_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_37.place(x=108+115, y=552+100)

milhao_min_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_38.place(x=108+138, y=552+100)

milhao_min_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
milhao_min_39.place(x=108+161, y=552+100)


lbl_porciento7 = Label(bg = color_fondo)
lbl_porciento7.place(x=108+116, y=503)
lbl_porciento7.config(font=('Arial',14))

lbl_cata_divisa7 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa7.place(x=108+44, y=515)
lbl_cata_divisa7.config(font=('Arial',7))

#_____________________________CATALOGO 8___________________________________________________________________
btn_milhao_max_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_0.place(x=318, y=552)

btn_milhao_max_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_1.place(x=318+23, y=552)

btn_milhao_max_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_2.place(x=318+46, y=552)

btn_milhao_max_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_3.place(x=318+69, y=552)

btn_milhao_max_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_4.place(x=318+92, y=552)

btn_milhao_max_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_5.place(x=318+115, y=552)

btn_milhao_max_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_6.place(x=318+138, y=552)

btn_milhao_max_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_7.place(x=318+161, y=552)

btn_milhao_max_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_8.place(x=318, y=552+25)

btn_milhao_max_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_9.place(x=318+23, y=552+25)

btn_milhao_max_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_10.place(x=318+46, y=552+25)

btn_milhao_max_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_11.place(x=318+69, y=552+25)

btn_milhao_max_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_12.place(x=318+92, y=552+25)

btn_milhao_max_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_13.place(x=318+115, y=552+25)

btn_milhao_max_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_14.place(x=318+138, y=552+25)

btn_milhao_max_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_15.place(x=318+161, y=552+25)

btn_milhao_max_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_16.place(x=318, y=552+50)

btn_milhao_max_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_17.place(x=318+23, y=552+50)

btn_milhao_max_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_18.place(x=318+46, y=552+50)

btn_milhao_max_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_19.place(x=318+69, y=552+50)

btn_milhao_max_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_20.place(x=318+92, y=552+50)

btn_milhao_max_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_21.place(x=318+115, y=552+50)

btn_milhao_max_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_22.place(x=318+138, y=552+50)

btn_milhao_max_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_23.place(x=318+161, y=552+50)

btn_milhao_max_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_24.place(x=318, y=552+75)

btn_milhao_max_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_25.place(x=318+23, y=552+75)

btn_milhao_max_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_26.place(x=318+46, y=552+75)

btn_milhao_max_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_27.place(x=318+69, y=552+75)

btn_milhao_max_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_28.place(x=318+92, y=552+75)

btn_milhao_max_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_29.place(x=318+115, y=552+75)

btn_milhao_max_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_30.place(x=318+138, y=552+75)

btn_milhao_max_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_31.place(x=318+161, y=552+75)

btn_milhao_max_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_32.place(x=318, y=552+100)

btn_milhao_max_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_33.place(x=318+23, y=552+100)

btn_milhao_max_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_34.place(x=318+46, y=552+100)

btn_milhao_max_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_35.place(x=318+69, y=552+100)

btn_milhao_max_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_36.place(x=318+92, y=552+100)

btn_milhao_max_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_37.place(x=318+115, y=552+100)

btn_milhao_max_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_38.place(x=318+138, y=552+100)

btn_milhao_max_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_milhao_max_39.place(x=318+161, y=552+100)

lbl_porciento8 = Label(bg = color_fondo)
lbl_porciento8.place(x=318+116, y=503)
lbl_porciento8.config(font=('Arial',14))

lbl_cata_divisa8 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa8.place(x=318+44, y=515)
lbl_cata_divisa8.config(font=('Arial',7))    
 
#_____________________________CATALOGO 9___________________________________________________________________
btn_torres_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_0.place(x=528, y=552)

btn_torres_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_1.place(x=528+23, y=552)

btn_torres_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_2.place(x=528+46, y=552)

btn_torres_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_3.place(x=528+69, y=552)

btn_torres_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_4.place(x=528+92, y=552)

btn_torres_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_5.place(x=528+115, y=552)

btn_torres_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_6.place(x=528+138, y=552)

btn_torres_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_7.place(x=528+161, y=552)

btn_torres_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_8.place(x=528, y=552+25)

btn_torres_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_9.place(x=528+23, y=552+25)

btn_torres_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_10.place(x=528+46, y=552+25)

btn_torres_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_11.place(x=528+69, y=552+25)

btn_torres_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_12.place(x=528+92, y=552+25)

btn_torres_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_13.place(x=528+115, y=552+25)

btn_torres_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_14.place(x=528+138, y=552+25)

btn_torres_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_15.place(x=528+161, y=552+25)

btn_torres_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_16.place(x=528, y=552+50)

btn_torres_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_17.place(x=528+23, y=552+50)

btn_torres_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_18.place(x=528+46, y=552+50)

btn_torres_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_19.place(x=528+69, y=552+50)

btn_torres_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_20.place(x=528+92, y=552+50)

btn_torres_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_21.place(x=528+115, y=552+50)

btn_torres_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_22.place(x=528+138, y=552+50)

btn_torres_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_23.place(x=528+161, y=552+50)

btn_torres_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_24.place(x=528, y=552+75)

btn_torres_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_25.place(x=528+23, y=552+75)

btn_torres_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_26.place(x=528+46, y=552+75)

btn_torres_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_27.place(x=528+69, y=552+75)

btn_torres_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_28.place(x=528+92, y=552+75)

btn_torres_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_29.place(x=528+115, y=552+75)

btn_torres_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_30.place(x=528+138, y=552+75)

btn_torres_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_31.place(x=528+161, y=552+75)

btn_torres_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_32.place(x=528, y=552+100)

btn_torres_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_33.place(x=528+23, y=552+100)

btn_torres_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_34.place(x=528+46, y=552+100)

btn_torres_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_35.place(x=528+69, y=552+100)

btn_torres_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_36.place(x=528+92, y=552+100)

btn_torres_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_37.place(x=528+115, y=552+100)

btn_torres_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_38.place(x=528+138, y=552+100)

btn_torres_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_torres_39.place(x=528+161, y=552+100)

lbl_porciento9 = Label(bg = color_fondo)
lbl_porciento9.place(x=528+116, y=503)
lbl_porciento9.config(font=('Arial',14))

lbl_cata_divisa9 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa9.place(x=528+44, y=515)
lbl_cata_divisa9.config(font=('Arial',7))



#_____________________________CATALOGO 10___________________________________________________________________
btn_padrao23_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_0.place(x=738, y=552)

btn_padrao23_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_1.place(x=738+23, y=552)

btn_padrao23_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_2.place(x=738+46, y=552)

btn_padrao23_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_3.place(x=738+69, y=552)

btn_padrao23_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_4.place(x=738+92, y=552)

btn_padrao23_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_5.place(x=738+115, y=552)

btn_padrao23_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_6.place(x=738+138, y=552)

btn_padrao23_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_7.place(x=738+161, y=552)

btn_padrao23_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_8.place(x=738, y=552+25)

btn_padrao23_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_9.place(x=738+23, y=552+25)

btn_padrao23_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_10.place(x=738+46, y=552+25)

btn_padrao23_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_11.place(x=738+69, y=552+25)

btn_padrao23_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_12.place(x=738+92, y=552+25)

btn_padrao23_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_13.place(x=738+115, y=552+25)

btn_padrao23_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_14.place(x=738+138, y=552+25)

btn_padrao23_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_15.place(x=738+161, y=552+25)

btn_padrao23_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_16.place(x=738, y=552+50)

btn_padrao23_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_17.place(x=738+23, y=552+50)

btn_padrao23_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_18.place(x=738+46, y=552+50)

btn_padrao23_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_19.place(x=738+69, y=552+50)

btn_padrao23_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_20.place(x=738+92, y=552+50)

btn_padrao23_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_21.place(x=738+115, y=552+50)

btn_padrao23_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_22.place(x=738+138, y=552+50)

btn_padrao23_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_23.place(x=738+161, y=552+50)

btn_padrao23_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_24.place(x=738, y=552+75)

btn_padrao23_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_25.place(x=738+23, y=552+75)

btn_padrao23_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_26.place(x=738+46, y=552+75)

btn_padrao23_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_27.place(x=738+69, y=552+75)

btn_padrao23_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_28.place(x=738+92, y=552+75)

btn_padrao23_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_29.place(x=738+115, y=552+75)

btn_padrao23_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_30.place(x=738+138, y=552+75)

btn_padrao23_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_31.place(x=738+161, y=552+75)

btn_padrao23_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_32.place(x=738, y=552+100)

btn_padrao23_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_33.place(x=738+23, y=552+100)

btn_padrao23_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_34.place(x=738+46, y=552+100)

btn_padrao23_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_35.place(x=738+69, y=552+100)

btn_padrao23_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_36.place(x=738+92, y=552+100)

btn_padrao23_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_37.place(x=738+115, y=552+100)

btn_padrao23_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_38.place(x=738+138, y=552+100)

btn_padrao23_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao23_39.place(x=738+161, y=552+100)

lbl_porciento10 = Label(bg = color_fondo)
lbl_porciento10.place(x=738+116, y=503)
lbl_porciento10.config(font=('Arial',14))

lbl_cata_divisa10 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa10.place(x=738+44, y=515)
lbl_cata_divisa10.config(font=('Arial',7))

#_____________________________CATALOGO 11___________________________________________________________________
btn_melhor_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_0.place(x=948, y=552)

btn_melhor_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_1.place(x=948+23, y=552)

btn_melhor_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_2.place(x=948+46, y=552)

btn_melhor_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_3.place(x=948+69, y=552)

btn_melhor_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_4.place(x=948+92, y=552)

btn_melhor_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_5.place(x=948+115, y=552)

btn_melhor_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_6.place(x=948+138, y=552)

btn_melhor_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_7.place(x=948+161, y=552)

btn_melhor_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_8.place(x=948, y=552+25)

btn_melhor_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_9.place(x=948+23, y=552+25)

btn_melhor_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_10.place(x=948+46, y=552+25)

btn_melhor_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_11.place(x=948+69, y=552+25)

btn_melhor_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_12.place(x=948+92, y=552+25)

btn_melhor_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_13.place(x=948+115, y=552+25)

btn_melhor_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_14.place(x=948+138, y=552+25)

btn_melhor_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_15.place(x=948+161, y=552+25)

btn_melhor_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_16.place(x=948, y=552+50)

btn_melhor_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_17.place(x=948+23, y=552+50)

btn_melhor_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_18.place(x=948+46, y=552+50)

btn_melhor_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_19.place(x=948+69, y=552+50)

btn_melhor_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_20.place(x=948+92, y=552+50)

btn_melhor_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_21.place(x=948+115, y=552+50)

btn_melhor_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_22.place(x=948+138, y=552+50)

btn_melhor_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_23.place(x=948+161, y=552+50)

btn_melhor_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_24.place(x=948, y=552+75)

btn_melhor_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_25.place(x=948+23, y=552+75)

btn_melhor_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_26.place(x=948+46, y=552+75)

btn_melhor_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_27.place(x=948+69, y=552+75)

btn_melhor_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_28.place(x=948+92, y=552+75)

btn_melhor_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_29.place(x=948+115, y=552+75)

btn_melhor_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_30.place(x=948+138, y=552+75)

btn_melhor_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_31.place(x=948+161, y=552+75)

btn_melhor_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_32.place(x=948, y=552+100)

btn_melhor_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_33.place(x=948+23, y=552+100)

btn_melhor_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_34.place(x=948+46, y=552+100)

btn_melhor_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_35.place(x=948+69, y=552+100)

btn_melhor_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_36.place(x=948+92, y=552+100)

btn_melhor_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_37.place(x=948+115, y=552+100)

btn_melhor_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_38.place(x=948+138, y=552+100)

btn_melhor_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_melhor_39.place(x=948+161, y=552+100)

lbl_porciento11 = Label(bg = color_fondo)
lbl_porciento11.place(x=948+116, y=503)
lbl_porciento11.config(font=('Arial',14))

lbl_cata_divisa11 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa11.place(x=948+44, y=515)
lbl_cata_divisa11.config(font=('Arial',7))

#_____________________________CATALOGO 12___________________________________________________________________
btn_padrao3x1_0 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_0.place(x=1158, y=552)

btn_padrao3x1_1 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_1.place(x=1158+23, y=552)

btn_padrao3x1_2 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_2.place(x=1158+46, y=552)

btn_padrao3x1_3 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_3.place(x=1158+69, y=552)

btn_padrao3x1_4 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_4.place(x=1158+92, y=552)

btn_padrao3x1_5 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_5.place(x=1158+115, y=552)

btn_padrao3x1_6 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_6.place(x=1158+138, y=552)

btn_padrao3x1_7 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_7.place(x=1158+161, y=552)

btn_padrao3x1_8 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_8.place(x=1158, y=552+25)

btn_padrao3x1_9 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_9.place(x=1158+23, y=552+25)

btn_padrao3x1_10 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_10.place(x=1158+46, y=552+25)

btn_padrao3x1_11 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_11.place(x=1158+69, y=552+25)

btn_padrao3x1_12 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_12.place(x=1158+92, y=552+25)

btn_padrao3x1_13 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_13.place(x=1158+115, y=552+25)

btn_padrao3x1_14 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_14.place(x=1158+138, y=552+25)

btn_padrao3x1_15 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_15.place(x=1158+161, y=552+25)

btn_padrao3x1_16 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_16.place(x=1158, y=552+50)

btn_padrao3x1_17 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_17.place(x=1158+23, y=552+50)

btn_padrao3x1_18 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_18.place(x=1158+46, y=552+50)

btn_padrao3x1_19 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_19.place(x=1158+69, y=552+50)

btn_padrao3x1_20 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_20.place(x=1158+92, y=552+50)

btn_padrao3x1_21 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_21.place(x=1158+115, y=552+50)

btn_padrao3x1_22 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_22.place(x=1158+138, y=552+50)

btn_padrao3x1_23 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_23.place(x=1158+161, y=552+50)

btn_padrao3x1_24 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_24.place(x=1158, y=552+75)

btn_padrao3x1_25 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_25.place(x=1158+23, y=552+75)

btn_padrao3x1_26 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_26.place(x=1158+46, y=552+75)

btn_padrao3x1_27 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_27.place(x=1158+69, y=552+75)

btn_padrao3x1_28 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_28.place(x=1158+92, y=552+75)

btn_padrao3x1_29 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_29.place(x=1158+115, y=552+75)

btn_padrao3x1_30 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_30.place(x=1158+138, y=552+75)

btn_padrao3x1_31 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_31.place(x=1158+161, y=552+75)

btn_padrao3x1_32 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_32.place(x=1158, y=552+100)

btn_padrao3x1_33 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_33.place(x=1158+23, y=552+100)

btn_padrao3x1_34 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_34.place(x=1158+46, y=552+100)

btn_padrao3x1_35 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_35.place(x=1158+69, y=552+100)

btn_padrao3x1_36 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_36.place(x=1158+92, y=552+100)

btn_padrao3x1_37 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_37.place(x=1158+115, y=552+100)

btn_padrao3x1_38 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_38.place(x=1158+138, y=552+100)

btn_padrao3x1_39 = Button(borderwidth = 0,height = 1, width = 2, bg = "white")
btn_padrao3x1_39.place(x=1158+161, y=552+100)

lbl_porciento12 = Label(bg = color_fondo)
lbl_porciento12.place(x=1158+116, y=503)
lbl_porciento12.config(font=('Arial',14))

lbl_cata_divisa12 = Label(bg = color_fondo, fg = "white")
lbl_cata_divisa12.place(x=1158+44, y=515)
lbl_cata_divisa12.config(font=('Arial',7))

########################################################BOTONES ESTADISTICAS#################################
lbl_estadisticas_win_1 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_1.place(x=153, y=317)
lbl_estadisticas_win_1.config(font=('Arial',7))

lbl_estadisticas_hit_1 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_1.place(x=190, y=317)
lbl_estadisticas_hit_1.config(font=('Arial',7))


lbl_estadisticas_g1_1 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_1.place(x=290, y=363)
lbl_estadisticas_g1_1.config(font=('Arial',6))

lbl_estadisticas_g2_1 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_1.place(x=290, y=363 + 26)
lbl_estadisticas_g2_1.config(font=('Arial',6))

lbl_estadisticas_g3_1 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_1.place(x=290, y=363 + 52)
lbl_estadisticas_g3_1.config(font=('Arial',6))

lbl_estadisticas_g4_1 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_1.place(x=290, y=363 + 78)
lbl_estadisticas_g4_1.config(font=('Arial',6))

lbl_estadisticas_g5_1 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_1.place(x=290, y=363 + 104)
lbl_estadisticas_g5_1.config(font=('Arial',6))

#__________________________mhi2____________________________________________________
lbl_estadisticas_win_2 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_2.place(x=153+210, y=317)
lbl_estadisticas_win_2.config(font=('Arial',7))

lbl_estadisticas_hit_2 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_2.place(x=190+210, y=317)
lbl_estadisticas_hit_2.config(font=('Arial',7))


lbl_estadisticas_g1_2 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_2.place(x=290+210, y=363)
lbl_estadisticas_g1_2.config(font=('Arial',6))

lbl_estadisticas_g2_2 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_2.place(x=290+210, y=363 + 26)
lbl_estadisticas_g2_2.config(font=('Arial',6))

lbl_estadisticas_g3_2 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_2.place(x=290+210, y=363 + 52)
lbl_estadisticas_g3_2.config(font=('Arial',6))

lbl_estadisticas_g4_2 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_2.place(x=290+210, y=363 + 78)
lbl_estadisticas_g4_2.config(font=('Arial',6))

lbl_estadisticas_g5_2 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_2.place(x=290+210, y=363 + 104)
lbl_estadisticas_g5_2.config(font=('Arial',6))

#__________________________mhi3____________________________________________________
lbl_estadisticas_win_3 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_3.place(x=153+420, y=317)
lbl_estadisticas_win_3.config(font=('Arial',7))

lbl_estadisticas_hit_3 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_3.place(x=190+420, y=317)
lbl_estadisticas_hit_3.config(font=('Arial',7))


lbl_estadisticas_g1_3 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_3.place(x=290+420, y=363)
lbl_estadisticas_g1_3.config(font=('Arial',6))

lbl_estadisticas_g2_3 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_3.place(x=290+420, y=363 + 26)
lbl_estadisticas_g2_3.config(font=('Arial',6))

lbl_estadisticas_g3_3 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_3.place(x=290+420, y=363 + 52)
lbl_estadisticas_g3_3.config(font=('Arial',6))

lbl_estadisticas_g4_3 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_3.place(x=290+420, y=363 + 78)
lbl_estadisticas_g4_3.config(font=('Arial',6))

lbl_estadisticas_g5_3 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_3.place(x=290+420, y=363 + 104)
lbl_estadisticas_g5_3.config(font=('Arial',6))

#__________________________mhimai____________________________________________________
lbl_estadisticas_win_4 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_4.place(x=153+630, y=317)
lbl_estadisticas_win_4.config(font=('Arial',7))

lbl_estadisticas_hit_4 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_4.place(x=190+630, y=317)
lbl_estadisticas_hit_4.config(font=('Arial',7))


lbl_estadisticas_g1_4 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_4.place(x=290+630, y=363)
lbl_estadisticas_g1_4.config(font=('Arial',6))

lbl_estadisticas_g2_4 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_4.place(x=290+630, y=363 + 26)
lbl_estadisticas_g2_4.config(font=('Arial',6))

lbl_estadisticas_g3_4 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_4.place(x=290+630, y=363 + 52)
lbl_estadisticas_g3_4.config(font=('Arial',6))

lbl_estadisticas_g4_4 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_4.place(x=290+630, y=363 + 78)
lbl_estadisticas_g4_4.config(font=('Arial',6))

lbl_estadisticas_g5_4 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_4.place(x=290+630, y=363 + 104)
lbl_estadisticas_g5_4.config(font=('Arial',6))

#__________________________mhi2mai____________________________________________________
lbl_estadisticas_win_5 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_5.place(x=153+840, y=317)
lbl_estadisticas_win_5.config(font=('Arial',7))

lbl_estadisticas_hit_5 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_5.place(x=190+840, y=317)
lbl_estadisticas_hit_5.config(font=('Arial',7))


lbl_estadisticas_g1_5 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_5.place(x=290+840, y=363)
lbl_estadisticas_g1_5.config(font=('Arial',6))

lbl_estadisticas_g2_5 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_5.place(x=290+840, y=363 + 26)
lbl_estadisticas_g2_5.config(font=('Arial',6))

lbl_estadisticas_g3_5 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_5.place(x=290+840, y=363 + 52)
lbl_estadisticas_g3_5.config(font=('Arial',6))

lbl_estadisticas_g4_5 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_5.place(x=290+840, y=363 + 78)
lbl_estadisticas_g4_5.config(font=('Arial',6))

lbl_estadisticas_g5_5 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_5.place(x=290+840, y=363 + 104)
lbl_estadisticas_g5_5.config(font=('Arial',6))

#__________________________mhi3mai____________________________________________________
lbl_estadisticas_win_6 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_6.place(x=153+1050, y=317)
lbl_estadisticas_win_6.config(font=('Arial',7))

lbl_estadisticas_hit_6 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_6.place(x=190+1050, y=317)
lbl_estadisticas_hit_6.config(font=('Arial',7))


lbl_estadisticas_g1_6 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_6.place(x=290+1050, y=363)
lbl_estadisticas_g1_6.config(font=('Arial',6))

lbl_estadisticas_g2_6 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_6.place(x=290+1050, y=363 + 26)
lbl_estadisticas_g2_6.config(font=('Arial',6))

lbl_estadisticas_g3_6 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_6.place(x=290+1050, y=363 + 52)
lbl_estadisticas_g3_6.config(font=('Arial',6))

lbl_estadisticas_g4_6 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_6.place(x=290+1050, y=363 + 78)
lbl_estadisticas_g4_6.config(font=('Arial',6))

lbl_estadisticas_g5_6 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_6.place(x=290+1050, y=363 + 104)
lbl_estadisticas_g5_6.config(font=('Arial',6))
####################PARTE DE ABAJO-milhao min###################################
lbl_estadisticas_win_7 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_7.place(x=153, y=502)
lbl_estadisticas_win_7.config(font=('Arial',7))

lbl_estadisticas_hit_7 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_7.place(x=190, y=502)
lbl_estadisticas_hit_7.config(font=('Arial',7))

lbl_estadisticas_g1_7 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_7.place(x=290, y=548)
lbl_estadisticas_g1_7.config(font=('Arial',6))

lbl_estadisticas_g2_7 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_7.place(x=290, y=548 + 26)
lbl_estadisticas_g2_7.config(font=('Arial',6))

lbl_estadisticas_g3_7 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_7.place(x=290, y=548 + 52)
lbl_estadisticas_g3_7.config(font=('Arial',6))

lbl_estadisticas_g4_7 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_7.place(x=290, y=548 + 78)
lbl_estadisticas_g4_7.config(font=('Arial',6))

lbl_estadisticas_g5_7 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_7.place(x=290, y=548 + 104)
lbl_estadisticas_g5_7.config(font=('Arial',6))

#__________________________milhao max____________________________________________________
lbl_estadisticas_win_8 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_8.place(x=153+210, y=502)
lbl_estadisticas_win_8.config(font=('Arial',7))

lbl_estadisticas_hit_8 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_8.place(x=190+210, y=502)
lbl_estadisticas_hit_8.config(font=('Arial',7))


lbl_estadisticas_g1_8 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_8.place(x=290+210, y=548)
lbl_estadisticas_g1_8.config(font=('Arial',6))

lbl_estadisticas_g2_8 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_8.place(x=290+210, y=548 + 26)
lbl_estadisticas_g2_8.config(font=('Arial',6))

lbl_estadisticas_g3_8 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_8.place(x=290+210, y=548 + 52)
lbl_estadisticas_g3_8.config(font=('Arial',6))

lbl_estadisticas_g4_8 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_8.place(x=290+210, y=548 + 78)
lbl_estadisticas_g4_8.config(font=('Arial',6))

lbl_estadisticas_g5_8 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_8.place(x=290+210, y=548 + 104)
lbl_estadisticas_g5_8.config(font=('Arial',6))

#__________________________torres____________________________________________________
lbl_estadisticas_win_9 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_9.place(x=153+420, y=502)
lbl_estadisticas_win_9.config(font=('Arial',7))

lbl_estadisticas_hit_9 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_9.place(x=190+420, y=502)
lbl_estadisticas_hit_9.config(font=('Arial',7))


lbl_estadisticas_g1_9 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_9.place(x=290+420, y=548)
lbl_estadisticas_g1_9.config(font=('Arial',6))

lbl_estadisticas_g2_9 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_9.place(x=290+420, y=548 + 26)
lbl_estadisticas_g2_9.config(font=('Arial',6))

lbl_estadisticas_g3_9 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_9.place(x=290+420, y=548 + 52)
lbl_estadisticas_g3_9.config(font=('Arial',6))

lbl_estadisticas_g4_9 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_9.place(x=290+420, y=548 + 78)
lbl_estadisticas_g4_9.config(font=('Arial',6))

lbl_estadisticas_g5_9 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_9.place(x=290+420, y=548 + 104)
lbl_estadisticas_g5_9.config(font=('Arial',6))

#__________________________padrao 23____________________________________________________
lbl_estadisticas_win_10 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_10.place(x=153+630, y=502)
lbl_estadisticas_win_10.config(font=('Arial',7))

lbl_estadisticas_hit_10 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_10.place(x=190+630, y=502)
lbl_estadisticas_hit_10.config(font=('Arial',7))


lbl_estadisticas_g1_10 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_10.place(x=290+630, y=548)
lbl_estadisticas_g1_10.config(font=('Arial',6))

lbl_estadisticas_g2_10 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_10.place(x=290+630, y=548 + 26)
lbl_estadisticas_g2_10.config(font=('Arial',6))

lbl_estadisticas_g3_10 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_10.place(x=290+630, y=548 + 52)
lbl_estadisticas_g3_10.config(font=('Arial',6))

lbl_estadisticas_g4_10 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_10.place(x=290+630, y=548 + 78)
lbl_estadisticas_g4_10.config(font=('Arial',6))

lbl_estadisticas_g5_10 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_10.place(x=290+630, y=548 + 104)
lbl_estadisticas_g5_10.config(font=('Arial',6))

#__________________________melhor de 3____________________________________________________
lbl_estadisticas_win_11 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_11.place(x=153+840, y=502)
lbl_estadisticas_win_11.config(font=('Arial',7))

lbl_estadisticas_hit_11 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_11.place(x=190+840, y=502)
lbl_estadisticas_hit_11.config(font=('Arial',7))


lbl_estadisticas_g1_11 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_11.place(x=290+840, y=548)
lbl_estadisticas_g1_11.config(font=('Arial',6))

lbl_estadisticas_g2_11 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_11.place(x=290+840, y=548 + 26)
lbl_estadisticas_g2_11.config(font=('Arial',6))

lbl_estadisticas_g3_11 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_11.place(x=290+840, y=548 + 52)
lbl_estadisticas_g3_11.config(font=('Arial',6))

lbl_estadisticas_g4_11 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_11.place(x=290+840, y=548 + 78)
lbl_estadisticas_g4_11.config(font=('Arial',6))

lbl_estadisticas_g5_11 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_11.place(x=290+840, y=548 + 104)
lbl_estadisticas_g5_11.config(font=('Arial',6))

#__________________________padrao 3x1____________________________________________________
lbl_estadisticas_win_12 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_win_12.place(x=153+1050, y=502)
lbl_estadisticas_win_12.config(font=('Arial',7))

lbl_estadisticas_hit_12 = Label(bg = color_fondo, fg = "indianred2")
lbl_estadisticas_hit_12.place(x=190+1050, y=502)
lbl_estadisticas_hit_12.config(font=('Arial',7))


lbl_estadisticas_g1_12 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g1_12.place(x=290+1050, y=548)
lbl_estadisticas_g1_12.config(font=('Arial',6))

lbl_estadisticas_g2_12 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g2_12.place(x=290+1050, y=548 + 26)
lbl_estadisticas_g2_12.config(font=('Arial',6))

lbl_estadisticas_g3_12 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g3_12.place(x=290+1050, y=548 + 52)
lbl_estadisticas_g3_12.config(font=('Arial',6))

lbl_estadisticas_g4_12 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g4_12.place(x=290+1050, y=548 + 78)
lbl_estadisticas_g4_12.config(font=('Arial',6))

lbl_estadisticas_g5_12 = Label(bg = color_fondo, fg = "white")
lbl_estadisticas_g5_12.place(x=290+1050, y=548 + 104)
lbl_estadisticas_g5_12.config(font=('Arial',6)) 

#__________________________estadisticas totales____________________________________________________
lbl_estadisticas_win_total = Label(bg = color_fondo)
lbl_estadisticas_win_total.place(x=106, y=680)
lbl_estadisticas_win_total.config(font=('Arial',8))

lbl_estadisticas_uno_total = Label(bg = color_fondo)
lbl_estadisticas_uno_total.place(x=106+114, y=680)
lbl_estadisticas_uno_total.config(font=('Arial',8))

lbl_estadisticas_dos_total = Label(bg = color_fondo)
lbl_estadisticas_dos_total.place(x=106+175, y=680)
lbl_estadisticas_dos_total.config(font=('Arial',8))

lbl_estadisticas_tres_total = Label(bg = color_fondo)
lbl_estadisticas_tres_total.place(x=106+236 , y=680)
lbl_estadisticas_tres_total.config(font=('Arial',8))

lbl_estadisticas_cuatro_total = Label(bg = color_fondo)
lbl_estadisticas_cuatro_total.place(x=106+297, y=680)
lbl_estadisticas_cuatro_total.config(font=('Arial',8))

lbl_estadisticas_cinco_total = Label(bg = color_fondo)
lbl_estadisticas_cinco_total.place(x=106+358, y=680)
lbl_estadisticas_cinco_total.config(font=('Arial',8))

lbl_estadisticas_seis_total = Label(bg = color_fondo)
lbl_estadisticas_seis_total.place(x=106+419, y=680)
lbl_estadisticas_seis_total.config(font=('Arial',8)) 

lbl_estadisticas_hora = Label(bg = color_fondo)
lbl_estadisticas_hora.place(x=106+991, y=680)
lbl_estadisticas_hora.config(font=('Arial',8)) 

def operacion1(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_mhi_0.config(bg = color[0],text=puntos[0])
  btn_mhi_1.config(bg = color[1],text=puntos[1])
  btn_mhi_2.config(bg = color[2],text=puntos[2])
  btn_mhi_3.config(bg = color[3],text=puntos[3])
  btn_mhi_4.config(bg = color[4],text=puntos[4])
  btn_mhi_5.config(bg = color[5],text=puntos[5])
  btn_mhi_6.config(bg = color[6],text=puntos[6])
  btn_mhi_7.config(bg = color[7],text=puntos[7])
  btn_mhi_8.config(bg = color[8],text=puntos[8])
  btn_mhi_9.config(bg = color[9],text=puntos[9])
  btn_mhi_10.config(bg = color[10],text=puntos[10])
  btn_mhi_11.config(bg = color[11],text=puntos[11])
  btn_mhi_12.config(bg = color[12],text=puntos[12])
  btn_mhi_13.config(bg = color[13],text=puntos[13])
  btn_mhi_14.config(bg = color[14],text=puntos[14])
  btn_mhi_15.config(bg = color[15],text=puntos[15])
  btn_mhi_16.config(bg = color[16],text=puntos[16])
  btn_mhi_17.config(bg = color[17],text=puntos[17])
  btn_mhi_18.config(bg = color[18],text=puntos[18])
  btn_mhi_19.config(bg = color[19],text=puntos[19])
  btn_mhi_20.config(bg = color[20],text=puntos[20])
  btn_mhi_21.config(bg = color[21],text=puntos[21])
  btn_mhi_22.config(bg = color[22],text=puntos[22])
  btn_mhi_23.config(bg = color[23],text=puntos[23])
  btn_mhi_24.config(bg = color[24],text=puntos[24])
  btn_mhi_25.config(bg = color[25],text=puntos[25])
  btn_mhi_26.config(bg = color[26],text=puntos[26])
  btn_mhi_27.config(bg = color[27],text=puntos[27])
  btn_mhi_28.config(bg = color[28],text=puntos[28])
  btn_mhi_29.config(bg = color[29],text=puntos[29])
  btn_mhi_30.config(bg = color[30],text=puntos[30])
  btn_mhi_31.config(bg = color[31],text=puntos[31])
  btn_mhi_32.config(bg = color[32],text=puntos[32])
  btn_mhi_33.config(bg = color[33],text=puntos[33])
  btn_mhi_34.config(bg = color[34],text=puntos[34])
  btn_mhi_35.config(bg = color[35],text=puntos[35])
  btn_mhi_36.config(bg = color[36],text=puntos[36])
  btn_mhi_37.config(bg = color[37],text=puntos[37])
  btn_mhi_38.config(bg = color[38],text=puntos[38])
  btn_mhi_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img1.config(image=seleccionar_foto(divisa))
  
  lbl_porciento1.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa1.config(text = divisa)
  
  n = 0
  global win_1
  global hit_1
  global g1_1
  global g2_1
  global g3_1
  global g4_1
  global g5_1
  win_1 = 0
  hit_1 = 0
  g1_1 = 0
  g2_1 = 0
  g3_1 = 0
  g4_1 = 0
  g5_1 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_1 = win_1 + 1
       if puntos[n] == "G1":
         g1_1 = g1_1 + 1
       if puntos[n] == "G2":
         g2_1 = g2_1 + 1
       if puntos[n] == "G3":
         g3_1 = g3_1 + 1  
       if puntos[n] == "G4":
         g4_1 = g4_1 + 1
       if puntos[n] == "G5":
         g5_1 = g5_1 + 1
       n = n + 1  
  g1_1st = str(g1_1)
  g2_1st = str(g2_1)
  g3_1st = str(g3_1)
  g4_1st = str(g4_1)
  g5_1st = str(g5_1)
  win_1 = round(((porciento_final / 100) * 40)- (g1_1 + g2_1 + g3_1 + g4_1 + g5_1)) 
  hit_1 = (40 - (win_1 + g1_1 + g2_1 + g3_1 + g4_1 + g5_1))
  win_1st = str(win_1)
  hit_1st = str(hit_1)
  if martin_gala == 0:
    lbl_estadisticas_win_1.config(text = "Win: " + win_1st)
    lbl_estadisticas_hit_1.config(text = "Hit: " + hit_1st)
    lbl_estadisticas_g1_1.config(text = "")
    lbl_estadisticas_g2_1.config(text = "")
    lbl_estadisticas_g3_1.config(text = "")
    lbl_estadisticas_g4_1.config(text = "")
    lbl_estadisticas_g5_1.config(text = "")
    
    
  if martin_gala == 1:
    lbl_estadisticas_win_1.config(text = "Win: " + win_1st)
    lbl_estadisticas_hit_1.config(text = "Hit: " + hit_1st)
    lbl_estadisticas_g1_1.config(text = "G1\n" + g1_1st)
    lbl_estadisticas_g2_1.config(text = "")
    lbl_estadisticas_g3_1.config(text = "")
    lbl_estadisticas_g4_1.config(text = "")
    lbl_estadisticas_g5_1.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_1.config(text = "Win: " + win_1st)
    lbl_estadisticas_hit_1.config(text = "Hit: " + hit_1st)       
    lbl_estadisticas_g1_1.config(text = "G1\n" + g1_1st)
    lbl_estadisticas_g2_1.config(text = "G2\n" + g2_1st)
    lbl_estadisticas_g3_1.config(text = "")
    lbl_estadisticas_g4_1.config(text = "")
    lbl_estadisticas_g5_1.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_1.config(text = "Win: " + win_1st)
    lbl_estadisticas_hit_1.config(text = "Hit: " + hit_1st)  
    lbl_estadisticas_g1_1.config(text = "G1\n" + g1_1st)
    lbl_estadisticas_g2_1.config(text = "G2\n" + g2_1st)
    lbl_estadisticas_g3_1.config(text = "G3\n" + g3_1st) 
    lbl_estadisticas_g4_1.config(text = "")
    lbl_estadisticas_g5_1.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_1.config(text = "Win: " + win_1st)
    lbl_estadisticas_hit_1.config(text = "Hit: " + hit_1st)  
    lbl_estadisticas_g1_1.config(text = "G1\n" + g1_1st)
    lbl_estadisticas_g2_1.config(text = "G2\n" + g2_1st)
    lbl_estadisticas_g3_1.config(text = "G3\n" + g3_1st)
    lbl_estadisticas_g4_1.config(text = "G4\n" + g4_1st)
    lbl_estadisticas_g5_1.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_1.config(text = "Win: " + win_1st)
    lbl_estadisticas_hit_1.config(text = "Hit: " + hit_1st)  
    lbl_estadisticas_g1_1.config(text = "G1\n" + g1_1st)
    lbl_estadisticas_g2_1.config(text = "G2\n" + g2_1st)
    lbl_estadisticas_g3_1.config(text = "G3\n" + g3_1st)
    lbl_estadisticas_g4_1.config(text = "G4\n" + g4_1st)
    lbl_estadisticas_g5_1.config(text = "G5\n" + g5_1st) 
    
        
def operacion2(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_mhi2_0.config(bg = color[0],text=puntos[0])
  btn_mhi2_1.config(bg = color[1],text=puntos[1])
  btn_mhi2_2.config(bg = color[2],text=puntos[2])
  btn_mhi2_3.config(bg = color[3],text=puntos[3])
  btn_mhi2_4.config(bg = color[4],text=puntos[4])
  btn_mhi2_5.config(bg = color[5],text=puntos[5])
  btn_mhi2_6.config(bg = color[6],text=puntos[6])
  btn_mhi2_7.config(bg = color[7],text=puntos[7])
  btn_mhi2_8.config(bg = color[8],text=puntos[8])
  btn_mhi2_9.config(bg = color[9],text=puntos[9])
  btn_mhi2_10.config(bg = color[10],text=puntos[10])
  btn_mhi2_11.config(bg = color[11],text=puntos[11])
  btn_mhi2_12.config(bg = color[12],text=puntos[12])
  btn_mhi2_13.config(bg = color[13],text=puntos[13])
  btn_mhi2_14.config(bg = color[14],text=puntos[14])
  btn_mhi2_15.config(bg = color[15],text=puntos[15])
  btn_mhi2_16.config(bg = color[16],text=puntos[16])
  btn_mhi2_17.config(bg = color[17],text=puntos[17])
  btn_mhi2_18.config(bg = color[18],text=puntos[18])
  btn_mhi2_19.config(bg = color[19],text=puntos[19])
  btn_mhi2_20.config(bg = color[20],text=puntos[20])
  btn_mhi2_21.config(bg = color[21],text=puntos[21])
  btn_mhi2_22.config(bg = color[22],text=puntos[22])
  btn_mhi2_23.config(bg = color[23],text=puntos[23])
  btn_mhi2_24.config(bg = color[24],text=puntos[24])
  btn_mhi2_25.config(bg = color[25],text=puntos[25])
  btn_mhi2_26.config(bg = color[26],text=puntos[26])
  btn_mhi2_27.config(bg = color[27],text=puntos[27])
  btn_mhi2_28.config(bg = color[28],text=puntos[28])
  btn_mhi2_29.config(bg = color[29],text=puntos[29])
  btn_mhi2_30.config(bg = color[30],text=puntos[30])
  btn_mhi2_31.config(bg = color[31],text=puntos[31])
  btn_mhi2_32.config(bg = color[32],text=puntos[32])
  btn_mhi2_33.config(bg = color[33],text=puntos[33])
  btn_mhi2_34.config(bg = color[34],text=puntos[34])
  btn_mhi2_35.config(bg = color[35],text=puntos[35])
  btn_mhi2_36.config(bg = color[36],text=puntos[36])
  btn_mhi2_37.config(bg = color[37],text=puntos[37])
  btn_mhi2_38.config(bg = color[38],text=puntos[38])
  btn_mhi2_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img2.config(image=seleccionar_foto(divisa))
  
  lbl_porciento2.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa2.config(text = divisa) 
  global win_2
  global hit_2
  global g1_2
  global g2_2
  global g3_2
  global g4_2
  global g5_2
  n = 0
  win_2 = 0
  hit_2 = 0
  g1_2 = 0
  g2_2 = 0
  g3_2 = 0
  g4_2 = 0
  g5_2 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_2 = win_2 + 1
       if puntos[n] == "G1":
         g1_2 = g1_2 + 1
       if puntos[n] == "G2":
         g2_2 = g2_2 + 1
       if puntos[n] == "G3":
         g3_2 = g3_2 + 1  
       if puntos[n] == "G4":
         g4_2 = g4_2 + 1
       if puntos[n] == "G5":
         g5_2 = g5_2 + 1
       n = n + 1  
  g1_2st = str(g1_2)
  g2_2st = str(g2_2)
  g3_2st = str(g3_2)
  g4_2st = str(g4_2)
  g5_2st = str(g5_2)
  win_2 = round(((porciento_final / 100) * 40)- (g1_2 + g2_2 + g3_2 + g4_2 + g5_2)) 
  hit_2 = (40 - (win_2 + g1_2 + g2_2 + g3_2 + g4_2 + g5_2))
  win_2st = str(win_2)
  hit_2st = str(hit_2)
  if martin_gala == 0:
    lbl_estadisticas_win_2.config(text = "Win: " + win_2st)
    lbl_estadisticas_hit_2.config(text = "Hit: " + hit_2st)
    lbl_estadisticas_g1_2.config(text = "")
    lbl_estadisticas_g2_2.config(text = "")
    lbl_estadisticas_g3_2.config(text = "")
    lbl_estadisticas_g4_2.config(text = "")
    lbl_estadisticas_g5_2.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_2.config(text = "Win: " + win_2st)
    lbl_estadisticas_hit_2.config(text = "Hit: " + hit_2st)
    lbl_estadisticas_g1_2.config(text = "G1\n" + g1_2st)
    lbl_estadisticas_g2_2.config(text = "")
    lbl_estadisticas_g3_2.config(text = "")
    lbl_estadisticas_g4_2.config(text = "")
    lbl_estadisticas_g5_2.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_2.config(text = "Win: " + win_2st)
    lbl_estadisticas_hit_2.config(text = "Hit: " + hit_2st)       
    lbl_estadisticas_g1_2.config(text = "G1\n" + g1_2st)
    lbl_estadisticas_g2_2.config(text = "G2\n" + g2_2st)
    lbl_estadisticas_g3_2.config(text = "")
    lbl_estadisticas_g4_2.config(text = "")
    lbl_estadisticas_g5_2.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_2.config(text = "Win: " + win_2st)
    lbl_estadisticas_hit_2.config(text = "Hit: " + hit_2st)  
    lbl_estadisticas_g1_2.config(text = "G1\n" + g1_2st)
    lbl_estadisticas_g2_2.config(text = "G2\n" + g2_2st)
    lbl_estadisticas_g3_2.config(text = "G3\n" + g3_2st) 
    lbl_estadisticas_g4_2.config(text = "")
    lbl_estadisticas_g5_2.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_2.config(text = "Win: " + win_2st)
    lbl_estadisticas_hit_2.config(text = "Hit: " + hit_2st)  
    lbl_estadisticas_g1_2.config(text = "G1\n" + g1_2st)
    lbl_estadisticas_g2_2.config(text = "G2\n" + g2_2st)
    lbl_estadisticas_g3_2.config(text = "G3\n" + g3_2st)
    lbl_estadisticas_g4_2.config(text = "G4\n" + g4_2st)
    lbl_estadisticas_g5_2.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_2.config(text = "Win: " + win_2st)
    lbl_estadisticas_hit_2.config(text = "Hit: " + hit_2st)  
    lbl_estadisticas_g1_2.config(text = "G1\n" + g1_2st)
    lbl_estadisticas_g2_2.config(text = "G2\n" + g2_2st)
    lbl_estadisticas_g3_2.config(text = "G3\n" + g3_2st)
    lbl_estadisticas_g4_2.config(text = "G4\n" + g4_2st)
    lbl_estadisticas_g5_2.config(text = "G5\n" + g5_2st)   
  
def operacion3(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_mhi3_0.config(bg = color[0],text=puntos[0])
  btn_mhi3_1.config(bg = color[1],text=puntos[1])
  btn_mhi3_2.config(bg = color[2],text=puntos[2])
  btn_mhi3_3.config(bg = color[3],text=puntos[3])
  btn_mhi3_4.config(bg = color[4],text=puntos[4])
  btn_mhi3_5.config(bg = color[5],text=puntos[5])
  btn_mhi3_6.config(bg = color[6],text=puntos[6])
  btn_mhi3_7.config(bg = color[7],text=puntos[7])
  btn_mhi3_8.config(bg = color[8],text=puntos[8])
  btn_mhi3_9.config(bg = color[9],text=puntos[9])
  btn_mhi3_10.config(bg = color[10],text=puntos[10])
  btn_mhi3_11.config(bg = color[11],text=puntos[11])
  btn_mhi3_12.config(bg = color[12],text=puntos[12])
  btn_mhi3_13.config(bg = color[13],text=puntos[13])
  btn_mhi3_14.config(bg = color[14],text=puntos[14])
  btn_mhi3_15.config(bg = color[15],text=puntos[15])
  btn_mhi3_16.config(bg = color[16],text=puntos[16])
  btn_mhi3_17.config(bg = color[17],text=puntos[17])
  btn_mhi3_18.config(bg = color[18],text=puntos[18])
  btn_mhi3_19.config(bg = color[19],text=puntos[19])
  btn_mhi3_20.config(bg = color[20],text=puntos[20])
  btn_mhi3_21.config(bg = color[21],text=puntos[21])
  btn_mhi3_22.config(bg = color[22],text=puntos[22])
  btn_mhi3_23.config(bg = color[23],text=puntos[23])
  btn_mhi3_24.config(bg = color[24],text=puntos[24])
  btn_mhi3_25.config(bg = color[25],text=puntos[25])
  btn_mhi3_26.config(bg = color[26],text=puntos[26])
  btn_mhi3_27.config(bg = color[27],text=puntos[27])
  btn_mhi3_28.config(bg = color[28],text=puntos[28])
  btn_mhi3_29.config(bg = color[29],text=puntos[29])
  btn_mhi3_30.config(bg = color[30],text=puntos[30])
  btn_mhi3_31.config(bg = color[31],text=puntos[31])
  btn_mhi3_32.config(bg = color[32],text=puntos[32])
  btn_mhi3_33.config(bg = color[33],text=puntos[33])
  btn_mhi3_34.config(bg = color[34],text=puntos[34])
  btn_mhi3_35.config(bg = color[35],text=puntos[35])
  btn_mhi3_36.config(bg = color[36],text=puntos[36])
  btn_mhi3_37.config(bg = color[37],text=puntos[37])
  btn_mhi3_38.config(bg = color[38],text=puntos[38])
  btn_mhi3_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img3.config(image=seleccionar_foto(divisa))
  
  lbl_porciento3.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa3.config(text = divisa) 
  global win_3
  global hit_3
  global g1_3
  global g2_3
  global g3_3
  global g4_3
  global g5_3
  n = 0
  win_3 = 0
  hit_3 = 0
  g1_3 = 0
  g2_3 = 0
  g3_3 = 0
  g4_3 = 0
  g5_3 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_3 = win_3 + 1
       if puntos[n] == "G1":
         g1_3 = g1_3 + 1
       if puntos[n] == "G2":
         g2_3 = g2_3 + 1
       if puntos[n] == "G3":
         g3_3 = g3_3 + 1  
       if puntos[n] == "G4":
         g4_3 = g4_3 + 1
       if puntos[n] == "G5":
         g5_3 = g5_3 + 1
       n = n + 1  
  g1_3st = str(g1_3)
  g2_3st = str(g2_3)
  g3_3st = str(g3_3)
  g4_3st = str(g4_3)
  g5_3st = str(g5_3)
  win_3 = round(((porciento_final / 100) * 40)- (g1_3 + g2_3 + g3_3 + g4_3 + g5_3)) 
  hit_3 = (40 - (win_3 + g1_3 + g2_3 + g3_3 + g4_3 + g5_3))
  win_3st = str(win_3)
  hit_3st = str(hit_3)
  if martin_gala == 0:
    lbl_estadisticas_win_3.config(text = "Win: " + win_3st)
    lbl_estadisticas_hit_3.config(text = "Hit: " + hit_3st)
    lbl_estadisticas_g1_3.config(text = "")
    lbl_estadisticas_g2_3.config(text = "")
    lbl_estadisticas_g3_3.config(text = "")
    lbl_estadisticas_g4_3.config(text = "")
    lbl_estadisticas_g5_3.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_3.config(text = "Win: " + win_3st)
    lbl_estadisticas_hit_3.config(text = "Hit: " + hit_3st)
    lbl_estadisticas_g1_3.config(text = "G1\n" + g1_3st)
    lbl_estadisticas_g2_3.config(text = "")
    lbl_estadisticas_g3_3.config(text = "")
    lbl_estadisticas_g4_3.config(text = "")
    lbl_estadisticas_g5_3.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_3.config(text = "Win: " + win_3st)
    lbl_estadisticas_hit_3.config(text = "Hit: " + hit_3st)       
    lbl_estadisticas_g1_3.config(text = "G1\n" + g1_3st)
    lbl_estadisticas_g2_3.config(text = "G2\n" + g2_3st)
    lbl_estadisticas_g3_3.config(text = "")
    lbl_estadisticas_g4_3.config(text = "")
    lbl_estadisticas_g5_3.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_3.config(text = "Win: " + win_3st)
    lbl_estadisticas_hit_3.config(text = "Hit: " + hit_3st)  
    lbl_estadisticas_g1_3.config(text = "G1\n" + g1_3st)
    lbl_estadisticas_g2_3.config(text = "G2\n" + g2_3st)
    lbl_estadisticas_g3_3.config(text = "G3\n" + g3_3st) 
    lbl_estadisticas_g4_3.config(text = "")
    lbl_estadisticas_g5_3.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_3.config(text = "Win: " + win_3st)
    lbl_estadisticas_hit_3.config(text = "Hit: " + hit_3st)  
    lbl_estadisticas_g1_3.config(text = "G1\n" + g1_3st)
    lbl_estadisticas_g2_3.config(text = "G2\n" + g2_3st)
    lbl_estadisticas_g3_3.config(text = "G3\n" + g3_3st)
    lbl_estadisticas_g4_3.config(text = "G4\n" + g4_3st)
    lbl_estadisticas_g5_3.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_3.config(text = "Win: " + win_3st)
    lbl_estadisticas_hit_3.config(text = "Hit: " + hit_3st)  
    lbl_estadisticas_g1_3.config(text = "G1\n" + g1_3st)
    lbl_estadisticas_g2_3.config(text = "G2\n" + g2_3st)
    lbl_estadisticas_g3_3.config(text = "G3\n" + g3_3st)
    lbl_estadisticas_g4_3.config(text = "G4\n" + g4_3st)
    lbl_estadisticas_g5_3.config(text = "G5\n" + g5_3st)

def operacion4(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_mhi_mai_0.config(bg = color[0],text=puntos[0])
  btn_mhi_mai_1.config(bg = color[1],text=puntos[1])
  btn_mhi_mai_2.config(bg = color[2],text=puntos[2])
  btn_mhi_mai_3.config(bg = color[3],text=puntos[3])
  btn_mhi_mai_4.config(bg = color[4],text=puntos[4])
  btn_mhi_mai_5.config(bg = color[5],text=puntos[5])
  btn_mhi_mai_6.config(bg = color[6],text=puntos[6])
  btn_mhi_mai_7.config(bg = color[7],text=puntos[7])
  btn_mhi_mai_8.config(bg = color[8],text=puntos[8])
  btn_mhi_mai_9.config(bg = color[9],text=puntos[9])
  btn_mhi_mai_10.config(bg = color[10],text=puntos[10])
  btn_mhi_mai_11.config(bg = color[11],text=puntos[11])
  btn_mhi_mai_12.config(bg = color[12],text=puntos[12])
  btn_mhi_mai_13.config(bg = color[13],text=puntos[13])
  btn_mhi_mai_14.config(bg = color[14],text=puntos[14])
  btn_mhi_mai_15.config(bg = color[15],text=puntos[15])
  btn_mhi_mai_16.config(bg = color[16],text=puntos[16])
  btn_mhi_mai_17.config(bg = color[17],text=puntos[17])
  btn_mhi_mai_18.config(bg = color[18],text=puntos[18])
  btn_mhi_mai_19.config(bg = color[19],text=puntos[19])
  btn_mhi_mai_20.config(bg = color[20],text=puntos[20])
  btn_mhi_mai_21.config(bg = color[21],text=puntos[21])
  btn_mhi_mai_22.config(bg = color[22],text=puntos[22])
  btn_mhi_mai_23.config(bg = color[23],text=puntos[23])
  btn_mhi_mai_24.config(bg = color[24],text=puntos[24])
  btn_mhi_mai_25.config(bg = color[25],text=puntos[25])
  btn_mhi_mai_26.config(bg = color[26],text=puntos[26])
  btn_mhi_mai_27.config(bg = color[27],text=puntos[27])
  btn_mhi_mai_28.config(bg = color[28],text=puntos[28])
  btn_mhi_mai_29.config(bg = color[29],text=puntos[29])
  btn_mhi_mai_30.config(bg = color[30],text=puntos[30])
  btn_mhi_mai_31.config(bg = color[31],text=puntos[31])
  btn_mhi_mai_32.config(bg = color[32],text=puntos[32])
  btn_mhi_mai_33.config(bg = color[33],text=puntos[33])
  btn_mhi_mai_34.config(bg = color[34],text=puntos[34])
  btn_mhi_mai_35.config(bg = color[35],text=puntos[35])
  btn_mhi_mai_36.config(bg = color[36],text=puntos[36])
  btn_mhi_mai_37.config(bg = color[37],text=puntos[37])
  btn_mhi_mai_38.config(bg = color[38],text=puntos[38])
  btn_mhi_mai_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img4.config(image=seleccionar_foto(divisa))
  
  lbl_porciento4.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa4.config(text = divisa)  
  global win_4
  global hit_4
  global g1_4
  global g2_4
  global g3_4
  global g4_4
  global g5_4
  n = 0
  win_4 = 0
  hit_4 = 0
  g1_4 = 0
  g2_4 = 0
  g3_4 = 0
  g4_4 = 0
  g5_4 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_4 = win_4 + 1
       if puntos[n] == "G1":
         g1_4 = g1_4 + 1
       if puntos[n] == "G2":
         g2_4 = g2_4 + 1
       if puntos[n] == "G3":
         g3_4 = g3_4 + 1  
       if puntos[n] == "G4":
         g4_4 = g4_4 + 1
       if puntos[n] == "G5":
         g5_4 = g5_4 + 1
       n = n + 1  
  g1_4st = str(g1_4)
  g2_4st = str(g2_4)
  g3_4st = str(g3_4)
  g4_4st = str(g4_4)
  g5_4st = str(g5_4)
  win_4 = round(((porciento_final / 100) * 40)- (g1_4 + g2_4 + g3_4 + g4_4 + g5_4)) 
  hit_4 = (40 - (win_4 + g1_4 + g2_4 + g3_4 + g4_4 + g5_4))
  win_4st = str(win_4)
  hit_4st = str(hit_4)
  if martin_gala == 0:
    lbl_estadisticas_win_4.config(text = "Win: " + win_4st)
    lbl_estadisticas_hit_4.config(text = "Hit: " + hit_4st)
    lbl_estadisticas_g1_4.config(text = "")
    lbl_estadisticas_g2_4.config(text = "")
    lbl_estadisticas_g3_4.config(text = "")
    lbl_estadisticas_g4_4.config(text = "")
    lbl_estadisticas_g5_4.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_4.config(text = "Win: " + win_4st)
    lbl_estadisticas_hit_4.config(text = "Hit: " + hit_4st)
    lbl_estadisticas_g1_4.config(text = "G1\n" + g1_4st)
    lbl_estadisticas_g2_4.config(text = "")
    lbl_estadisticas_g3_4.config(text = "")
    lbl_estadisticas_g4_4.config(text = "")
    lbl_estadisticas_g5_4.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_4.config(text = "Win: " + win_4st)
    lbl_estadisticas_hit_4.config(text = "Hit: " + hit_4st)       
    lbl_estadisticas_g1_4.config(text = "G1\n" + g1_4st)
    lbl_estadisticas_g2_4.config(text = "G2\n" + g2_4st)
    lbl_estadisticas_g3_4.config(text = "")
    lbl_estadisticas_g4_4.config(text = "")
    lbl_estadisticas_g5_4.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_4.config(text = "Win: " + win_4st)
    lbl_estadisticas_hit_4.config(text = "Hit: " + hit_4st)  
    lbl_estadisticas_g1_4.config(text = "G1\n" + g1_4st)
    lbl_estadisticas_g2_4.config(text = "G2\n" + g2_4st)
    lbl_estadisticas_g3_4.config(text = "G3\n" + g3_4st) 
    lbl_estadisticas_g4_4.config(text = "")
    lbl_estadisticas_g5_4.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_4.config(text = "Win: " + win_4st)
    lbl_estadisticas_hit_4.config(text = "Hit: " + hit_4st)  
    lbl_estadisticas_g1_4.config(text = "G1\n" + g1_4st)
    lbl_estadisticas_g2_4.config(text = "G2\n" + g2_4st)
    lbl_estadisticas_g3_4.config(text = "G3\n" + g3_4st)
    lbl_estadisticas_g4_4.config(text = "G4\n" + g4_4st)
    lbl_estadisticas_g5_4.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_4.config(text = "Win: " + win_4st)
    lbl_estadisticas_hit_4.config(text = "Hit: " + hit_4st)  
    lbl_estadisticas_g1_4.config(text = "G1\n" + g1_4st)
    lbl_estadisticas_g2_4.config(text = "G2\n" + g2_4st)
    lbl_estadisticas_g3_4.config(text = "G3\n" + g3_4st)
    lbl_estadisticas_g4_4.config(text = "G4\n" + g4_4st)
    lbl_estadisticas_g5_4.config(text = "G5\n" + g5_4st)
def operacion5(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_mhi2_mai_0.config(bg = color[0],text=puntos[0])
  btn_mhi2_mai_1.config(bg = color[1],text=puntos[1])
  btn_mhi2_mai_2.config(bg = color[2],text=puntos[2])
  btn_mhi2_mai_3.config(bg = color[3],text=puntos[3])
  btn_mhi2_mai_4.config(bg = color[4],text=puntos[4])
  btn_mhi2_mai_5.config(bg = color[5],text=puntos[5])
  btn_mhi2_mai_6.config(bg = color[6],text=puntos[6])
  btn_mhi2_mai_7.config(bg = color[7],text=puntos[7])
  btn_mhi2_mai_8.config(bg = color[8],text=puntos[8])
  btn_mhi2_mai_9.config(bg = color[9],text=puntos[9])
  btn_mhi2_mai_10.config(bg = color[10],text=puntos[10])
  btn_mhi2_mai_11.config(bg = color[11],text=puntos[11])
  btn_mhi2_mai_12.config(bg = color[12],text=puntos[12])
  btn_mhi2_mai_13.config(bg = color[13],text=puntos[13])
  btn_mhi2_mai_14.config(bg = color[14],text=puntos[14])
  btn_mhi2_mai_15.config(bg = color[15],text=puntos[15])
  btn_mhi2_mai_16.config(bg = color[16],text=puntos[16])
  btn_mhi2_mai_17.config(bg = color[17],text=puntos[17])
  btn_mhi2_mai_18.config(bg = color[18],text=puntos[18])
  btn_mhi2_mai_19.config(bg = color[19],text=puntos[19])
  btn_mhi2_mai_20.config(bg = color[20],text=puntos[20])
  btn_mhi2_mai_21.config(bg = color[21],text=puntos[21])
  btn_mhi2_mai_22.config(bg = color[22],text=puntos[22])
  btn_mhi2_mai_23.config(bg = color[23],text=puntos[23])
  btn_mhi2_mai_24.config(bg = color[24],text=puntos[24])
  btn_mhi2_mai_25.config(bg = color[25],text=puntos[25])
  btn_mhi2_mai_26.config(bg = color[26],text=puntos[26])
  btn_mhi2_mai_27.config(bg = color[27],text=puntos[27])
  btn_mhi2_mai_28.config(bg = color[28],text=puntos[28])
  btn_mhi2_mai_29.config(bg = color[29],text=puntos[29])
  btn_mhi2_mai_30.config(bg = color[30],text=puntos[30])
  btn_mhi2_mai_31.config(bg = color[31],text=puntos[31])
  btn_mhi2_mai_32.config(bg = color[32],text=puntos[32])
  btn_mhi2_mai_33.config(bg = color[33],text=puntos[33])
  btn_mhi2_mai_34.config(bg = color[34],text=puntos[34])
  btn_mhi2_mai_35.config(bg = color[35],text=puntos[35])
  btn_mhi2_mai_36.config(bg = color[36],text=puntos[36])
  btn_mhi2_mai_37.config(bg = color[37],text=puntos[37])
  btn_mhi2_mai_38.config(bg = color[38],text=puntos[38])
  btn_mhi2_mai_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img5.config(image=seleccionar_foto(divisa))
  
  lbl_porciento5.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa5.config(text = divisa)  
  global win_5
  global hit_5
  global g1_5
  global g2_5
  global g3_5
  global g4_5
  global g5_5
  n = 0
  win_5 = 0
  hit_5 = 0
  g1_5 = 0
  g2_5 = 0
  g3_5 = 0
  g4_5 = 0
  g5_5 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_5 = win_5 + 1
       if puntos[n] == "G1":
         g1_5 = g1_5 + 1
       if puntos[n] == "G2":
         g2_5 = g2_5 + 1
       if puntos[n] == "G3":
         g3_5 = g3_5 + 1  
       if puntos[n] == "G4":
         g4_5 = g4_5 + 1
       if puntos[n] == "G5":
         g5_5 = g5_5 + 1
       n = n + 1  
  g1_5st = str(g1_5)
  g2_5st = str(g2_5)
  g3_5st = str(g3_5)
  g4_5st = str(g4_5)
  g5_5st = str(g5_5)
  win_5 = round(((porciento_final / 100) * 40)- (g1_5 + g2_5 + g3_5 + g4_5 + g5_5)) 
  hit_5 = (40 - (win_5 + g1_5 + g2_5 + g3_5 + g4_5 + g5_5))
  win_5st = str(win_5)
  hit_5st = str(hit_5)
  if martin_gala == 0:
    lbl_estadisticas_win_5.config(text = "Win: " + win_5st)
    lbl_estadisticas_hit_5.config(text = "Hit: " + hit_5st)
    lbl_estadisticas_g1_5.config(text = "")
    lbl_estadisticas_g2_5.config(text = "")
    lbl_estadisticas_g3_5.config(text = "")
    lbl_estadisticas_g4_5.config(text = "")
    lbl_estadisticas_g5_5.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_5.config(text = "Win: " + win_5st)
    lbl_estadisticas_hit_5.config(text = "Hit: " + hit_5st)
    lbl_estadisticas_g1_5.config(text = "G1\n" + g1_5st)
    lbl_estadisticas_g2_5.config(text = "")
    lbl_estadisticas_g3_5.config(text = "")
    lbl_estadisticas_g4_5.config(text = "")
    lbl_estadisticas_g5_5.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_5.config(text = "Win: " + win_5st)
    lbl_estadisticas_hit_5.config(text = "Hit: " + hit_5st)       
    lbl_estadisticas_g1_5.config(text = "G1\n" + g1_5st)
    lbl_estadisticas_g2_5.config(text = "G2\n" + g2_5st)
    lbl_estadisticas_g3_5.config(text = "")
    lbl_estadisticas_g4_5.config(text = "")
    lbl_estadisticas_g5_5.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_5.config(text = "Win: " + win_5st)
    lbl_estadisticas_hit_5.config(text = "Hit: " + hit_5st)  
    lbl_estadisticas_g1_5.config(text = "G1\n" + g1_5st)
    lbl_estadisticas_g2_5.config(text = "G2\n" + g2_5st)
    lbl_estadisticas_g3_5.config(text = "G3\n" + g3_5st) 
    lbl_estadisticas_g4_5.config(text = "")
    lbl_estadisticas_g5_5.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_5.config(text = "Win: " + win_5st)
    lbl_estadisticas_hit_5.config(text = "Hit: " + hit_5st)  
    lbl_estadisticas_g1_5.config(text = "G1\n" + g1_5st)
    lbl_estadisticas_g2_5.config(text = "G2\n" + g2_5st)
    lbl_estadisticas_g3_5.config(text = "G3\n" + g3_5st)
    lbl_estadisticas_g4_5.config(text = "G4\n" + g4_5st)
    lbl_estadisticas_g5_5.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_5.config(text = "Win: " + win_5st)
    lbl_estadisticas_hit_5.config(text = "Hit: " + hit_5st)  
    lbl_estadisticas_g1_5.config(text = "G1\n" + g1_5st)
    lbl_estadisticas_g2_5.config(text = "G2\n" + g2_5st)
    lbl_estadisticas_g3_5.config(text = "G3\n" + g3_5st)
    lbl_estadisticas_g4_5.config(text = "G4\n" + g4_5st)
    lbl_estadisticas_g5_5.config(text = "G5\n" + g5_5st)
    
def operacion6(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_mhi3_mai_0.config(bg = color[0],text=puntos[0])
  btn_mhi3_mai_1.config(bg = color[1],text=puntos[1])
  btn_mhi3_mai_2.config(bg = color[2],text=puntos[2])
  btn_mhi3_mai_3.config(bg = color[3],text=puntos[3])
  btn_mhi3_mai_4.config(bg = color[4],text=puntos[4])
  btn_mhi3_mai_5.config(bg = color[5],text=puntos[5])
  btn_mhi3_mai_6.config(bg = color[6],text=puntos[6])
  btn_mhi3_mai_7.config(bg = color[7],text=puntos[7])
  btn_mhi3_mai_8.config(bg = color[8],text=puntos[8])
  btn_mhi3_mai_9.config(bg = color[9],text=puntos[9])
  btn_mhi3_mai_10.config(bg = color[10],text=puntos[10])
  btn_mhi3_mai_11.config(bg = color[11],text=puntos[11])
  btn_mhi3_mai_12.config(bg = color[12],text=puntos[12])
  btn_mhi3_mai_13.config(bg = color[13],text=puntos[13])
  btn_mhi3_mai_14.config(bg = color[14],text=puntos[14])
  btn_mhi3_mai_15.config(bg = color[15],text=puntos[15])
  btn_mhi3_mai_16.config(bg = color[16],text=puntos[16])
  btn_mhi3_mai_17.config(bg = color[17],text=puntos[17])
  btn_mhi3_mai_18.config(bg = color[18],text=puntos[18])
  btn_mhi3_mai_19.config(bg = color[19],text=puntos[19])
  btn_mhi3_mai_20.config(bg = color[20],text=puntos[20])
  btn_mhi3_mai_21.config(bg = color[21],text=puntos[21])
  btn_mhi3_mai_22.config(bg = color[22],text=puntos[22])
  btn_mhi3_mai_23.config(bg = color[23],text=puntos[23])
  btn_mhi3_mai_24.config(bg = color[24],text=puntos[24])
  btn_mhi3_mai_25.config(bg = color[25],text=puntos[25])
  btn_mhi3_mai_26.config(bg = color[26],text=puntos[26])
  btn_mhi3_mai_27.config(bg = color[27],text=puntos[27])
  btn_mhi3_mai_28.config(bg = color[28],text=puntos[28])
  btn_mhi3_mai_29.config(bg = color[29],text=puntos[29])
  btn_mhi3_mai_30.config(bg = color[30],text=puntos[30])
  btn_mhi3_mai_31.config(bg = color[31],text=puntos[31])
  btn_mhi3_mai_32.config(bg = color[32],text=puntos[32])
  btn_mhi3_mai_33.config(bg = color[33],text=puntos[33])
  btn_mhi3_mai_34.config(bg = color[34],text=puntos[34])
  btn_mhi3_mai_35.config(bg = color[35],text=puntos[35])
  btn_mhi3_mai_36.config(bg = color[36],text=puntos[36])
  btn_mhi3_mai_37.config(bg = color[37],text=puntos[37])
  btn_mhi3_mai_38.config(bg = color[38],text=puntos[38])
  btn_mhi3_mai_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img6.config(image=seleccionar_foto(divisa))
  
  lbl_porciento6.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa6.config(text = divisa) 
  global win_6
  global hit_6
  global g1_6
  global g2_6
  global g3_6
  global g4_6
  global g5_6
  n = 0
  win_6 = 0
  hit_6 = 0
  g1_6 = 0
  g2_6 = 0
  g3_6 = 0
  g4_6 = 0
  g5_6 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_6 = win_6 + 1
       if puntos[n] == "G1":
         g1_6 = g1_6 + 1
       if puntos[n] == "G2":
         g2_6 = g2_6 + 1
       if puntos[n] == "G3":
         g3_6 = g3_6 + 1  
       if puntos[n] == "G4":
         g4_6 = g4_6 + 1
       if puntos[n] == "G5":
         g5_6 = g5_6 + 1
       n = n + 1  
  g1_6st = str(g1_6)
  g2_6st = str(g2_6)
  g3_6st = str(g3_6)
  g4_6st = str(g4_6)
  g5_6st = str(g5_6)
  win_6 = round(((porciento_final / 100) * 40)- (g1_6 + g2_6 + g3_6 + g4_6 + g5_6)) 
  hit_6 = (40 - (win_6 + g1_6 + g2_6 + g3_6 + g4_6 + g5_6))
  win_6st = str(win_6)
  hit_6st = str(hit_6)
  if martin_gala == 0:
    lbl_estadisticas_win_6.config(text = "Win: " + win_6st)
    lbl_estadisticas_hit_6.config(text = "Hit: " + hit_6st)
    lbl_estadisticas_g1_6.config(text = "")
    lbl_estadisticas_g2_6.config(text = "")
    lbl_estadisticas_g3_6.config(text = "")
    lbl_estadisticas_g4_6.config(text = "")
    lbl_estadisticas_g5_6.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_6.config(text = "Win: " + win_6st)
    lbl_estadisticas_hit_6.config(text = "Hit: " + hit_6st)
    lbl_estadisticas_g1_6.config(text = "G1\n" + g1_6st)
    lbl_estadisticas_g2_6.config(text = "")
    lbl_estadisticas_g3_6.config(text = "")
    lbl_estadisticas_g4_6.config(text = "")
    lbl_estadisticas_g5_6.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_6.config(text = "Win: " + win_6st)
    lbl_estadisticas_hit_6.config(text = "Hit: " + hit_6st)       
    lbl_estadisticas_g1_6.config(text = "G1\n" + g1_6st)
    lbl_estadisticas_g2_6.config(text = "G2\n" + g2_6st)
    lbl_estadisticas_g3_6.config(text = "")
    lbl_estadisticas_g4_6.config(text = "")
    lbl_estadisticas_g5_6.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_6.config(text = "Win: " + win_6st)
    lbl_estadisticas_hit_6.config(text = "Hit: " + hit_6st)  
    lbl_estadisticas_g1_6.config(text = "G1\n" + g1_6st)
    lbl_estadisticas_g2_6.config(text = "G2\n" + g2_6st)
    lbl_estadisticas_g3_6.config(text = "G3\n" + g3_6st) 
    lbl_estadisticas_g4_6.config(text = "")
    lbl_estadisticas_g5_6.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_6.config(text = "Win: " + win_6st)
    lbl_estadisticas_hit_6.config(text = "Hit: " + hit_6st)  
    lbl_estadisticas_g1_6.config(text = "G1\n" + g1_6st)
    lbl_estadisticas_g2_6.config(text = "G2\n" + g2_6st)
    lbl_estadisticas_g3_6.config(text = "G3\n" + g3_6st)
    lbl_estadisticas_g4_6.config(text = "G4\n" + g4_6st)
    lbl_estadisticas_g5_6.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_6.config(text = "Win: " + win_6st)
    lbl_estadisticas_hit_6.config(text = "Hit: " + hit_6st)  
    lbl_estadisticas_g1_6.config(text = "G1\n" + g1_6st)
    lbl_estadisticas_g2_6.config(text = "G2\n" + g2_6st)
    lbl_estadisticas_g3_6.config(text = "G3\n" + g3_6st)
    lbl_estadisticas_g4_6.config(text = "G4\n" + g4_6st)
    lbl_estadisticas_g5_6.config(text = "G5\n" + g5_6st)

def operacion7(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  milhao_min_0.config(bg = color[0],text=puntos[0])
  milhao_min_1.config(bg = color[1],text=puntos[1])
  milhao_min_2.config(bg = color[2],text=puntos[2])
  milhao_min_3.config(bg = color[3],text=puntos[3])
  milhao_min_4.config(bg = color[4],text=puntos[4])
  milhao_min_5.config(bg = color[5],text=puntos[5])
  milhao_min_6.config(bg = color[6],text=puntos[6])
  milhao_min_7.config(bg = color[7],text=puntos[7])
  milhao_min_8.config(bg = color[8],text=puntos[8])
  milhao_min_9.config(bg = color[9],text=puntos[9])
  milhao_min_10.config(bg = color[10],text=puntos[10])
  milhao_min_11.config(bg = color[11],text=puntos[11])
  milhao_min_12.config(bg = color[12],text=puntos[12])
  milhao_min_13.config(bg = color[13],text=puntos[13])
  milhao_min_14.config(bg = color[14],text=puntos[14])
  milhao_min_15.config(bg = color[15],text=puntos[15])
  milhao_min_16.config(bg = color[16],text=puntos[16])
  milhao_min_17.config(bg = color[17],text=puntos[17])
  milhao_min_18.config(bg = color[18],text=puntos[18])
  milhao_min_19.config(bg = color[19],text=puntos[19])
  milhao_min_20.config(bg = color[20],text=puntos[20])
  milhao_min_21.config(bg = color[21],text=puntos[21])
  milhao_min_22.config(bg = color[22],text=puntos[22])
  milhao_min_23.config(bg = color[23],text=puntos[23])
  milhao_min_24.config(bg = color[24],text=puntos[24])
  milhao_min_25.config(bg = color[25],text=puntos[25])
  milhao_min_26.config(bg = color[26],text=puntos[26])
  milhao_min_27.config(bg = color[27],text=puntos[27])
  milhao_min_28.config(bg = color[28],text=puntos[28])
  milhao_min_29.config(bg = color[29],text=puntos[29])
  milhao_min_30.config(bg = color[30],text=puntos[30])
  milhao_min_31.config(bg = color[31],text=puntos[31])
  milhao_min_32.config(bg = color[32],text=puntos[32])
  milhao_min_33.config(bg = color[33],text=puntos[33])
  milhao_min_34.config(bg = color[34],text=puntos[34])
  milhao_min_35.config(bg = color[35],text=puntos[35])
  milhao_min_36.config(bg = color[36],text=puntos[36])
  milhao_min_37.config(bg = color[37],text=puntos[37])
  milhao_min_38.config(bg = color[38],text=puntos[38])
  milhao_min_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img7.config(image=seleccionar_foto(divisa))
  
  lbl_porciento7.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa7.config(text = divisa)
  global win_7
  global hit_7
  global g1_7
  global g2_7
  global g3_7
  global g4_7
  global g5_7
  n = 0
  win_7 = 0
  hit_7 = 0
  g1_7 = 0
  g2_7 = 0
  g3_7 = 0
  g4_7 = 0
  g5_7 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_7 = win_7 + 1
       if puntos[n] == "G1":
         g1_7 = g1_7 + 1
       if puntos[n] == "G2":
         g2_7 = g2_7 + 1
       if puntos[n] == "G3":
         g3_7 = g3_7 + 1  
       if puntos[n] == "G4":
         g4_7 = g4_7 + 1
       if puntos[n] == "G5":
         g5_7 = g5_7 + 1
       n = n + 1  
  g1_7st = str(g1_7)
  g2_7st = str(g2_7)
  g3_7st = str(g3_7)
  g4_7st = str(g4_7)
  g5_7st = str(g5_7)
  win_7 = round(((porciento_final / 100) * 40)- (g1_7 + g2_7 + g3_7 + g4_7 + g5_7)) 
  hit_7 = (40 - (win_7 + g1_7 + g2_7 + g3_7 + g4_7 + g5_7))
  win_7st = str(win_7)
  hit_7st = str(hit_7)
  if martin_gala == 0:
    lbl_estadisticas_win_7.config(text = "Win: " + win_7st)
    lbl_estadisticas_hit_7.config(text = "Hit: " + hit_7st)
    lbl_estadisticas_g1_7.config(text = "")
    lbl_estadisticas_g2_7.config(text = "")
    lbl_estadisticas_g3_7.config(text = "")
    lbl_estadisticas_g4_7.config(text = "")
    lbl_estadisticas_g5_7.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_7.config(text = "Win: " + win_7st)
    lbl_estadisticas_hit_7.config(text = "Hit: " + hit_7st)
    lbl_estadisticas_g1_7.config(text = "G1\n" + g1_7st)
    lbl_estadisticas_g2_7.config(text = "")
    lbl_estadisticas_g3_7.config(text = "")
    lbl_estadisticas_g4_7.config(text = "")
    lbl_estadisticas_g5_7.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_7.config(text = "Win: " + win_7st)
    lbl_estadisticas_hit_7.config(text = "Hit: " + hit_7st)       
    lbl_estadisticas_g1_7.config(text = "G1\n" + g1_7st)
    lbl_estadisticas_g2_7.config(text = "G2\n" + g2_7st)
    lbl_estadisticas_g3_7.config(text = "")
    lbl_estadisticas_g4_7.config(text = "")
    lbl_estadisticas_g5_7.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_7.config(text = "Win: " + win_7st)
    lbl_estadisticas_hit_7.config(text = "Hit: " + hit_7st)  
    lbl_estadisticas_g1_7.config(text = "G1\n" + g1_7st)
    lbl_estadisticas_g2_7.config(text = "G2\n" + g2_7st)
    lbl_estadisticas_g3_7.config(text = "G3\n" + g3_7st) 
    lbl_estadisticas_g4_7.config(text = "")
    lbl_estadisticas_g5_7.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_7.config(text = "Win: " + win_7st)
    lbl_estadisticas_hit_7.config(text = "Hit: " + hit_7st)  
    lbl_estadisticas_g1_7.config(text = "G1\n" + g1_7st)
    lbl_estadisticas_g2_7.config(text = "G2\n" + g2_7st)
    lbl_estadisticas_g3_7.config(text = "G3\n" + g3_7st)
    lbl_estadisticas_g4_7.config(text = "G4\n" + g4_7st)
    lbl_estadisticas_g5_7.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_7.config(text = "Win: " + win_7st)
    lbl_estadisticas_hit_7.config(text = "Hit: " + hit_7st)  
    lbl_estadisticas_g1_7.config(text = "G1\n" + g1_7st)
    lbl_estadisticas_g2_7.config(text = "G2\n" + g2_7st)
    lbl_estadisticas_g3_7.config(text = "G3\n" + g3_7st)
    lbl_estadisticas_g4_7.config(text = "G4\n" + g4_7st)
    lbl_estadisticas_g5_7.config(text = "G5\n" + g5_7st)
    
def operacion8(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_milhao_max_0.config(bg = color[0],text=puntos[0])
  btn_milhao_max_1.config(bg = color[1],text=puntos[1])
  btn_milhao_max_2.config(bg = color[2],text=puntos[2])
  btn_milhao_max_3.config(bg = color[3],text=puntos[3])
  btn_milhao_max_4.config(bg = color[4],text=puntos[4])
  btn_milhao_max_5.config(bg = color[5],text=puntos[5])
  btn_milhao_max_6.config(bg = color[6],text=puntos[6])
  btn_milhao_max_7.config(bg = color[7],text=puntos[7])
  btn_milhao_max_8.config(bg = color[8],text=puntos[8])
  btn_milhao_max_9.config(bg = color[9],text=puntos[9])
  btn_milhao_max_10.config(bg = color[10],text=puntos[10])
  btn_milhao_max_11.config(bg = color[11],text=puntos[11])
  btn_milhao_max_12.config(bg = color[12],text=puntos[12])
  btn_milhao_max_13.config(bg = color[13],text=puntos[13])
  btn_milhao_max_14.config(bg = color[14],text=puntos[14])
  btn_milhao_max_15.config(bg = color[15],text=puntos[15])
  btn_milhao_max_16.config(bg = color[16],text=puntos[16])
  btn_milhao_max_17.config(bg = color[17],text=puntos[17])
  btn_milhao_max_18.config(bg = color[18],text=puntos[18])
  btn_milhao_max_19.config(bg = color[19],text=puntos[19])
  btn_milhao_max_20.config(bg = color[20],text=puntos[20])
  btn_milhao_max_21.config(bg = color[21],text=puntos[21])
  btn_milhao_max_22.config(bg = color[22],text=puntos[22])
  btn_milhao_max_23.config(bg = color[23],text=puntos[23])
  btn_milhao_max_24.config(bg = color[24],text=puntos[24])
  btn_milhao_max_25.config(bg = color[25],text=puntos[25])
  btn_milhao_max_26.config(bg = color[26],text=puntos[26])
  btn_milhao_max_27.config(bg = color[27],text=puntos[27])
  btn_milhao_max_28.config(bg = color[28],text=puntos[28])
  btn_milhao_max_29.config(bg = color[29],text=puntos[29])
  btn_milhao_max_30.config(bg = color[30],text=puntos[30])
  btn_milhao_max_31.config(bg = color[31],text=puntos[31])
  btn_milhao_max_32.config(bg = color[32],text=puntos[32])
  btn_milhao_max_33.config(bg = color[33],text=puntos[33])
  btn_milhao_max_34.config(bg = color[34],text=puntos[34])
  btn_milhao_max_35.config(bg = color[35],text=puntos[35])
  btn_milhao_max_36.config(bg = color[36],text=puntos[36])
  btn_milhao_max_37.config(bg = color[37],text=puntos[37])
  btn_milhao_max_38.config(bg = color[38],text=puntos[38])
  btn_milhao_max_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img8.config(image=seleccionar_foto(divisa))
  
  lbl_porciento8.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa8.config(text = divisa)
  global win_8
  global hit_8
  global g1_8
  global g2_8
  global g3_8
  global g4_8
  global g5_8
  n = 0
  win_8 = 0
  hit_8 = 0
  g1_8 = 0
  g2_8 = 0
  g3_8 = 0
  g4_8 = 0
  g5_8 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_8 = win_8 + 1
       if puntos[n] == "G1":
         g1_8 = g1_8 + 1
       if puntos[n] == "G2":
         g2_8 = g2_8 + 1
       if puntos[n] == "G3":
         g3_8 = g3_8 + 1  
       if puntos[n] == "G4":
         g4_8 = g4_8 + 1
       if puntos[n] == "G5":
         g5_8 = g5_8 + 1
       n = n + 1  
  g1_8st = str(g1_8)
  g2_8st = str(g2_8)
  g3_8st = str(g3_8)
  g4_8st = str(g4_8)
  g5_8st = str(g5_8)
  win_8 = round(((porciento_final / 100) * 40)- (g1_8 + g2_8 + g3_8 + g4_8 + g5_8)) 
  hit_8 = (40 - (win_8 + g1_8 + g2_8 + g3_8 + g4_8 + g5_8))
  win_8st = str(win_8)
  hit_8st = str(hit_8)
  if martin_gala == 0:
    lbl_estadisticas_win_8.config(text = "Win: " + win_8st)
    lbl_estadisticas_hit_8.config(text = "Hit: " + hit_8st)
    lbl_estadisticas_g1_8.config(text = "")
    lbl_estadisticas_g2_8.config(text = "")
    lbl_estadisticas_g3_8.config(text = "")
    lbl_estadisticas_g4_8.config(text = "")
    lbl_estadisticas_g5_8.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_8.config(text = "Win: " + win_8st)
    lbl_estadisticas_hit_8.config(text = "Hit: " + hit_8st)
    lbl_estadisticas_g1_8.config(text = "G1\n" + g1_8st)
    lbl_estadisticas_g2_8.config(text = "")
    lbl_estadisticas_g3_8.config(text = "")
    lbl_estadisticas_g4_8.config(text = "")
    lbl_estadisticas_g5_8.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_8.config(text = "Win: " + win_8st)
    lbl_estadisticas_hit_8.config(text = "Hit: " + hit_8st)       
    lbl_estadisticas_g1_8.config(text = "G1\n" + g1_8st)
    lbl_estadisticas_g2_8.config(text = "G2\n" + g2_8st)
    lbl_estadisticas_g3_8.config(text = "")
    lbl_estadisticas_g4_8.config(text = "")
    lbl_estadisticas_g5_8.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_8.config(text = "Win: " + win_8st)
    lbl_estadisticas_hit_8.config(text = "Hit: " + hit_8st)  
    lbl_estadisticas_g1_8.config(text = "G1\n" + g1_8st)
    lbl_estadisticas_g2_8.config(text = "G2\n" + g2_8st)
    lbl_estadisticas_g3_8.config(text = "G3\n" + g3_8st) 
    lbl_estadisticas_g4_8.config(text = "")
    lbl_estadisticas_g5_8.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_8.config(text = "Win: " + win_8st)
    lbl_estadisticas_hit_8.config(text = "Hit: " + hit_8st)  
    lbl_estadisticas_g1_8.config(text = "G1\n" + g1_8st)
    lbl_estadisticas_g2_8.config(text = "G2\n" + g2_8st)
    lbl_estadisticas_g3_8.config(text = "G3\n" + g3_8st)
    lbl_estadisticas_g4_8.config(text = "G4\n" + g4_8st)
    lbl_estadisticas_g5_8.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_8.config(text = "Win: " + win_8st)
    lbl_estadisticas_hit_8.config(text = "Hit: " + hit_8st)  
    lbl_estadisticas_g1_8.config(text = "G1\n" + g1_8st)
    lbl_estadisticas_g2_8.config(text = "G2\n" + g2_8st)
    lbl_estadisticas_g3_8.config(text = "G3\n" + g3_8st)
    lbl_estadisticas_g4_8.config(text = "G4\n" + g4_8st)
    lbl_estadisticas_g5_8.config(text = "G5\n" + g5_8st)  

def operacion9(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_torres_0.config(bg = color[0],text=puntos[0])
  btn_torres_1.config(bg = color[1],text=puntos[1])
  btn_torres_2.config(bg = color[2],text=puntos[2])
  btn_torres_3.config(bg = color[3],text=puntos[3])
  btn_torres_4.config(bg = color[4],text=puntos[4])
  btn_torres_5.config(bg = color[5],text=puntos[5])
  btn_torres_6.config(bg = color[6],text=puntos[6])
  btn_torres_7.config(bg = color[7],text=puntos[7])
  btn_torres_8.config(bg = color[8],text=puntos[8])
  btn_torres_9.config(bg = color[9],text=puntos[9])
  btn_torres_10.config(bg = color[10],text=puntos[10])
  btn_torres_11.config(bg = color[11],text=puntos[11])
  btn_torres_12.config(bg = color[12],text=puntos[12])
  btn_torres_13.config(bg = color[13],text=puntos[13])
  btn_torres_14.config(bg = color[14],text=puntos[14])
  btn_torres_15.config(bg = color[15],text=puntos[15])
  btn_torres_16.config(bg = color[16],text=puntos[16])
  btn_torres_17.config(bg = color[17],text=puntos[17])
  btn_torres_18.config(bg = color[18],text=puntos[18])
  btn_torres_19.config(bg = color[19],text=puntos[19])
  btn_torres_20.config(bg = color[20],text=puntos[20])
  btn_torres_21.config(bg = color[21],text=puntos[21])
  btn_torres_22.config(bg = color[22],text=puntos[22])
  btn_torres_23.config(bg = color[23],text=puntos[23])
  btn_torres_24.config(bg = color[24],text=puntos[24])
  btn_torres_25.config(bg = color[25],text=puntos[25])
  btn_torres_26.config(bg = color[26],text=puntos[26])
  btn_torres_27.config(bg = color[27],text=puntos[27])
  btn_torres_28.config(bg = color[28],text=puntos[28])
  btn_torres_29.config(bg = color[29],text=puntos[29])
  btn_torres_30.config(bg = color[30],text=puntos[30])
  btn_torres_31.config(bg = color[31],text=puntos[31])
  btn_torres_32.config(bg = color[32],text=puntos[32])
  btn_torres_33.config(bg = color[33],text=puntos[33])
  btn_torres_34.config(bg = color[34],text=puntos[34])
  btn_torres_35.config(bg = color[35],text=puntos[35])
  btn_torres_36.config(bg = color[36],text=puntos[36])
  btn_torres_37.config(bg = color[37],text=puntos[37])
  btn_torres_38.config(bg = color[38],text=puntos[38])
  btn_torres_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img9.config(image=seleccionar_foto(divisa))
  
  lbl_porciento9.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa9.config(text = divisa) 
  global win_9
  global hit_9
  global g1_9
  global g2_9
  global g3_9
  global g4_9
  global g5_9
  n = 0
  win_9 = 0
  hit_9 = 0
  g1_9 = 0
  g2_9 = 0
  g3_9 = 0
  g4_9 = 0
  g5_9 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_9 = win_9 + 1
       if puntos[n] == "G1":
         g1_9 = g1_9 + 1
       if puntos[n] == "G2":
         g2_9 = g2_9 + 1
       if puntos[n] == "G3":
         g3_9 = g3_9 + 1  
       if puntos[n] == "G4":
         g4_9 = g4_9 + 1
       if puntos[n] == "G5":
         g5_9 = g5_9 + 1
       n = n + 1  
  g1_9st = str(g1_9)
  g2_9st = str(g2_9)
  g3_9st = str(g3_9)
  g4_9st = str(g4_9)
  g5_9st = str(g5_9)
  win_9 = round(((porciento_final / 100) * 40)- (g1_9 + g2_9 + g3_9 + g4_9 + g5_9)) 
  hit_9 = (40 - (win_9 + g1_9 + g2_9 + g3_9 + g4_9 + g5_9))
  win_9st = str(win_9)
  hit_9st = str(hit_9)
  if martin_gala == 0:
    lbl_estadisticas_win_9.config(text = "Win: " + win_9st)
    lbl_estadisticas_hit_9.config(text = "Hit: " + hit_9st)
    lbl_estadisticas_g1_9.config(text = "")
    lbl_estadisticas_g2_9.config(text = "")
    lbl_estadisticas_g3_9.config(text = "")
    lbl_estadisticas_g4_9.config(text = "")
    lbl_estadisticas_g5_9.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_9.config(text = "Win: " + win_9st)
    lbl_estadisticas_hit_9.config(text = "Hit: " + hit_9st)
    lbl_estadisticas_g1_9.config(text = "G1\n" + g1_9st)
    lbl_estadisticas_g2_9.config(text = "")
    lbl_estadisticas_g3_9.config(text = "")
    lbl_estadisticas_g4_9.config(text = "")
    lbl_estadisticas_g5_9.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_9.config(text = "Win: " + win_9st)
    lbl_estadisticas_hit_9.config(text = "Hit: " + hit_9st)       
    lbl_estadisticas_g1_9.config(text = "G1\n" + g1_9st)
    lbl_estadisticas_g2_9.config(text = "G2\n" + g2_9st)
    lbl_estadisticas_g3_9.config(text = "")
    lbl_estadisticas_g4_9.config(text = "")
    lbl_estadisticas_g5_9.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_9.config(text = "Win: " + win_9st)
    lbl_estadisticas_hit_9.config(text = "Hit: " + hit_9st)  
    lbl_estadisticas_g1_9.config(text = "G1\n" + g1_9st)
    lbl_estadisticas_g2_9.config(text = "G2\n" + g2_9st)
    lbl_estadisticas_g3_9.config(text = "G3\n" + g3_9st) 
    lbl_estadisticas_g4_9.config(text = "")
    lbl_estadisticas_g5_9.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_9.config(text = "Win: " + win_9st)
    lbl_estadisticas_hit_9.config(text = "Hit: " + hit_9st)  
    lbl_estadisticas_g1_9.config(text = "G1\n" + g1_9st)
    lbl_estadisticas_g2_9.config(text = "G2\n" + g2_9st)
    lbl_estadisticas_g3_9.config(text = "G3\n" + g3_9st)
    lbl_estadisticas_g4_9.config(text = "G4\n" + g4_9st)
    lbl_estadisticas_g5_9.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_9.config(text = "Win: " + win_9st)
    lbl_estadisticas_hit_9.config(text = "Hit: " + hit_9st)  
    lbl_estadisticas_g1_9.config(text = "G1\n" + g1_9st)
    lbl_estadisticas_g2_9.config(text = "G2\n" + g2_9st)
    lbl_estadisticas_g3_9.config(text = "G3\n" + g3_9st)
    lbl_estadisticas_g4_9.config(text = "G4\n" + g4_9st)
    lbl_estadisticas_g5_9.config(text = "G5\n" + g5_9st)

def operacion10(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_padrao23_0.config(bg = color[0],text=puntos[0])
  btn_padrao23_1.config(bg = color[1],text=puntos[1])
  btn_padrao23_2.config(bg = color[2],text=puntos[2])
  btn_padrao23_3.config(bg = color[3],text=puntos[3])
  btn_padrao23_4.config(bg = color[4],text=puntos[4])
  btn_padrao23_5.config(bg = color[5],text=puntos[5])
  btn_padrao23_6.config(bg = color[6],text=puntos[6])
  btn_padrao23_7.config(bg = color[7],text=puntos[7])
  btn_padrao23_8.config(bg = color[8],text=puntos[8])
  btn_padrao23_9.config(bg = color[9],text=puntos[9])
  btn_padrao23_10.config(bg = color[10],text=puntos[10])
  btn_padrao23_11.config(bg = color[11],text=puntos[11])
  btn_padrao23_12.config(bg = color[12],text=puntos[12])
  btn_padrao23_13.config(bg = color[13],text=puntos[13])
  btn_padrao23_14.config(bg = color[14],text=puntos[14])
  btn_padrao23_15.config(bg = color[15],text=puntos[15])
  btn_padrao23_16.config(bg = color[16],text=puntos[16])
  btn_padrao23_17.config(bg = color[17],text=puntos[17])
  btn_padrao23_18.config(bg = color[18],text=puntos[18])
  btn_padrao23_19.config(bg = color[19],text=puntos[19])
  btn_padrao23_20.config(bg = color[20],text=puntos[20])
  btn_padrao23_21.config(bg = color[21],text=puntos[21])
  btn_padrao23_22.config(bg = color[22],text=puntos[22])
  btn_padrao23_23.config(bg = color[23],text=puntos[23])
  btn_padrao23_24.config(bg = color[24],text=puntos[24])
  btn_padrao23_25.config(bg = color[25],text=puntos[25])
  btn_padrao23_26.config(bg = color[26],text=puntos[26])
  btn_padrao23_27.config(bg = color[27],text=puntos[27])
  btn_padrao23_28.config(bg = color[28],text=puntos[28])
  btn_padrao23_29.config(bg = color[29],text=puntos[29])
  btn_padrao23_30.config(bg = color[30],text=puntos[30])
  btn_padrao23_31.config(bg = color[31],text=puntos[31])
  btn_padrao23_32.config(bg = color[32],text=puntos[32])
  btn_padrao23_33.config(bg = color[33],text=puntos[33])
  btn_padrao23_34.config(bg = color[34],text=puntos[34])
  btn_padrao23_35.config(bg = color[35],text=puntos[35])
  btn_padrao23_36.config(bg = color[36],text=puntos[36])
  btn_padrao23_37.config(bg = color[37],text=puntos[37])
  btn_padrao23_38.config(bg = color[38],text=puntos[38])
  btn_padrao23_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img10.config(image=seleccionar_foto(divisa))
  
  lbl_porciento10.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa10.config(text = divisa)
  global win_10
  global hit_10
  global g1_10
  global g2_10
  global g3_10
  global g4_10
  global g5_10
  n = 0
  win_10 = 0
  hit_10 = 0
  g1_10 = 0
  g2_10 = 0
  g3_10 = 0
  g4_10 = 0
  g5_10 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_10 = win_10 + 1
       if puntos[n] == "G1":
         g1_10 = g1_10 + 1
       if puntos[n] == "G2":
         g2_10 = g2_10 + 1
       if puntos[n] == "G3":
         g3_10 = g3_10 + 1  
       if puntos[n] == "G4":
         g4_10 = g4_10 + 1
       if puntos[n] == "G5":
         g5_10 = g5_10 + 1
       n = n + 1  
  g1_10st = str(g1_10)
  g2_10st = str(g2_10)
  g3_10st = str(g3_10)
  g4_10st = str(g4_10)
  g5_10st = str(g5_10)
  win_10 = round(((porciento_final / 100) * 40)- (g1_10 + g2_10 + g3_10 + g4_10 + g5_10)) 
  hit_10 = (40 - (win_10 + g1_10 + g2_10 + g3_10 + g4_10 + g5_10))
  win_10st = str(win_10)
  hit_10st = str(hit_10)
  if martin_gala == 0:
    lbl_estadisticas_win_10.config(text = "Win: " + win_10st)
    lbl_estadisticas_hit_10.config(text = "Hit: " + hit_10st)
    lbl_estadisticas_g1_10.config(text = "")
    lbl_estadisticas_g2_10.config(text = "")
    lbl_estadisticas_g3_10.config(text = "")
    lbl_estadisticas_g4_10.config(text = "")
    lbl_estadisticas_g5_10.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_10.config(text = "Win: " + win_10st)
    lbl_estadisticas_hit_10.config(text = "Hit: " + hit_10st)
    lbl_estadisticas_g1_10.config(text = "G1\n" + g1_10st)
    lbl_estadisticas_g2_10.config(text = "")
    lbl_estadisticas_g3_10.config(text = "")
    lbl_estadisticas_g4_10.config(text = "")
    lbl_estadisticas_g5_10.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_10.config(text = "Win: " + win_10st)
    lbl_estadisticas_hit_10.config(text = "Hit: " + hit_10st)       
    lbl_estadisticas_g1_10.config(text = "G1\n" + g1_10st)
    lbl_estadisticas_g2_10.config(text = "G2\n" + g2_10st)
    lbl_estadisticas_g3_10.config(text = "")
    lbl_estadisticas_g4_10.config(text = "")
    lbl_estadisticas_g5_10.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_10.config(text = "Win: " + win_10st)
    lbl_estadisticas_hit_10.config(text = "Hit: " + hit_10st)  
    lbl_estadisticas_g1_10.config(text = "G1\n" + g1_10st)
    lbl_estadisticas_g2_10.config(text = "G2\n" + g2_10st)
    lbl_estadisticas_g3_10.config(text = "G3\n" + g3_10st) 
    lbl_estadisticas_g4_10.config(text = "")
    lbl_estadisticas_g5_10.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_10.config(text = "Win: " + win_10st)
    lbl_estadisticas_hit_10.config(text = "Hit: " + hit_10st)  
    lbl_estadisticas_g1_10.config(text = "G1\n" + g1_10st)
    lbl_estadisticas_g2_10.config(text = "G2\n" + g2_10st)
    lbl_estadisticas_g3_10.config(text = "G3\n" + g3_10st)
    lbl_estadisticas_g4_10.config(text = "G4\n" + g4_10st)
    lbl_estadisticas_g5_10.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_10.config(text = "Win: " + win_10st)
    lbl_estadisticas_hit_10.config(text = "Hit: " + hit_10st)  
    lbl_estadisticas_g1_10.config(text = "G1\n" + g1_10st)
    lbl_estadisticas_g2_10.config(text = "G2\n" + g2_10st)
    lbl_estadisticas_g3_10.config(text = "G3\n" + g3_10st)
    lbl_estadisticas_g4_10.config(text = "G4\n" + g4_10st)
    lbl_estadisticas_g5_10.config(text = "G5\n" + g5_10st)  


def operacion11(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_melhor_0.config(bg = color[0],text=puntos[0])
  btn_melhor_1.config(bg = color[1],text=puntos[1])
  btn_melhor_2.config(bg = color[2],text=puntos[2])
  btn_melhor_3.config(bg = color[3],text=puntos[3])
  btn_melhor_4.config(bg = color[4],text=puntos[4])
  btn_melhor_5.config(bg = color[5],text=puntos[5])
  btn_melhor_6.config(bg = color[6],text=puntos[6])
  btn_melhor_7.config(bg = color[7],text=puntos[7])
  btn_melhor_8.config(bg = color[8],text=puntos[8])
  btn_melhor_9.config(bg = color[9],text=puntos[9])
  btn_melhor_10.config(bg = color[10],text=puntos[10])
  btn_melhor_11.config(bg = color[11],text=puntos[11])
  btn_melhor_12.config(bg = color[12],text=puntos[12])
  btn_melhor_13.config(bg = color[13],text=puntos[13])
  btn_melhor_14.config(bg = color[14],text=puntos[14])
  btn_melhor_15.config(bg = color[15],text=puntos[15])
  btn_melhor_16.config(bg = color[16],text=puntos[16])
  btn_melhor_17.config(bg = color[17],text=puntos[17])
  btn_melhor_18.config(bg = color[18],text=puntos[18])
  btn_melhor_19.config(bg = color[19],text=puntos[19])
  btn_melhor_20.config(bg = color[20],text=puntos[20])
  btn_melhor_21.config(bg = color[21],text=puntos[21])
  btn_melhor_22.config(bg = color[22],text=puntos[22])
  btn_melhor_23.config(bg = color[23],text=puntos[23])
  btn_melhor_24.config(bg = color[24],text=puntos[24])
  btn_melhor_25.config(bg = color[25],text=puntos[25])
  btn_melhor_26.config(bg = color[26],text=puntos[26])
  btn_melhor_27.config(bg = color[27],text=puntos[27])
  btn_melhor_28.config(bg = color[28],text=puntos[28])
  btn_melhor_29.config(bg = color[29],text=puntos[29])
  btn_melhor_30.config(bg = color[30],text=puntos[30])
  btn_melhor_31.config(bg = color[31],text=puntos[31])
  btn_melhor_32.config(bg = color[32],text=puntos[32])
  btn_melhor_33.config(bg = color[33],text=puntos[33])
  btn_melhor_34.config(bg = color[34],text=puntos[34])
  btn_melhor_35.config(bg = color[35],text=puntos[35])
  btn_melhor_36.config(bg = color[36],text=puntos[36])
  btn_melhor_37.config(bg = color[37],text=puntos[37])
  btn_melhor_38.config(bg = color[38],text=puntos[38])
  btn_melhor_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img11.config(image=seleccionar_foto(divisa))
  
  lbl_porciento11.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa11.config(text = divisa)  
  global win_11
  global hit_11
  global g1_11
  global g2_11
  global g3_11
  global g4_11
  global g5_11
  n = 0
  win_11 = 0
  hit_11 = 0
  g1_11 = 0
  g2_11 = 0
  g3_11 = 0
  g4_11 = 0
  g5_11 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_11 = win_11 + 1
       if puntos[n] == "G1":
         g1_11 = g1_11 + 1
       if puntos[n] == "G2":
         g2_11 = g2_11 + 1
       if puntos[n] == "G3":
         g3_11 = g3_11 + 1  
       if puntos[n] == "G4":
         g4_11 = g4_11 + 1
       if puntos[n] == "G5":
         g5_11 = g5_11 + 1
       n = n + 1  
  g1_11st = str(g1_11)
  g2_11st = str(g2_11)
  g3_11st = str(g3_11)
  g4_11st = str(g4_11)
  g5_11st = str(g5_11)
  win_11 = round(((porciento_final / 100) * 40)- (g1_11 + g2_11 + g3_11 + g4_11 + g5_11)) 
  hit_11 = (40 - (win_11 + g1_11 + g2_11 + g3_11 + g4_11 + g5_11))
  win_11st = str(win_11)
  hit_11st = str(hit_11)
  if martin_gala == 0:
    lbl_estadisticas_win_11.config(text = "Win: " + win_11st)
    lbl_estadisticas_hit_11.config(text = "Hit: " + hit_11st)
    lbl_estadisticas_g1_11.config(text = "")
    lbl_estadisticas_g2_11.config(text = "")
    lbl_estadisticas_g3_11.config(text = "")
    lbl_estadisticas_g4_11.config(text = "")
    lbl_estadisticas_g5_11.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_11.config(text = "Win: " + win_11st)
    lbl_estadisticas_hit_11.config(text = "Hit: " + hit_11st)
    lbl_estadisticas_g1_11.config(text = "G1\n" + g1_11st)
    lbl_estadisticas_g2_11.config(text = "")
    lbl_estadisticas_g3_11.config(text = "")
    lbl_estadisticas_g4_11.config(text = "")
    lbl_estadisticas_g5_11.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_11.config(text = "Win: " + win_11st)
    lbl_estadisticas_hit_11.config(text = "Hit: " + hit_11st)       
    lbl_estadisticas_g1_11.config(text = "G1\n" + g1_11st)
    lbl_estadisticas_g2_11.config(text = "G2\n" + g2_11st)
    lbl_estadisticas_g3_11.config(text = "")
    lbl_estadisticas_g4_11.config(text = "")
    lbl_estadisticas_g5_11.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_11.config(text = "Win: " + win_11st)
    lbl_estadisticas_hit_11.config(text = "Hit: " + hit_11st)  
    lbl_estadisticas_g1_11.config(text = "G1\n" + g1_11st)
    lbl_estadisticas_g2_11.config(text = "G2\n" + g2_11st)
    lbl_estadisticas_g3_11.config(text = "G3\n" + g3_11st) 
    lbl_estadisticas_g4_11.config(text = "")
    lbl_estadisticas_g5_11.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_11.config(text = "Win: " + win_11st)
    lbl_estadisticas_hit_11.config(text = "Hit: " + hit_11st)  
    lbl_estadisticas_g1_11.config(text = "G1\n" + g1_11st)
    lbl_estadisticas_g2_11.config(text = "G2\n" + g2_11st)
    lbl_estadisticas_g3_11.config(text = "G3\n" + g3_11st)
    lbl_estadisticas_g4_11.config(text = "G4\n" + g4_11st)
    lbl_estadisticas_g5_11.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_11.config(text = "Win: " + win_11st)
    lbl_estadisticas_hit_11.config(text = "Hit: " + hit_11st)  
    lbl_estadisticas_g1_11.config(text = "G1\n" + g1_11st)
    lbl_estadisticas_g2_11.config(text = "G2\n" + g2_11st)
    lbl_estadisticas_g3_11.config(text = "G3\n" + g3_11st)
    lbl_estadisticas_g4_11.config(text = "G4\n" + g4_11st)
    lbl_estadisticas_g5_11.config(text = "G5\n" + g5_11st)
    
def operacion12(color,puntos,porciento_final,fg_porciento,divisa,martin_gala):    

  btn_padrao3x1_0.config(bg = color[0],text=puntos[0])
  btn_padrao3x1_1.config(bg = color[1],text=puntos[1])
  btn_padrao3x1_2.config(bg = color[2],text=puntos[2])
  btn_padrao3x1_3.config(bg = color[3],text=puntos[3])
  btn_padrao3x1_4.config(bg = color[4],text=puntos[4])
  btn_padrao3x1_5.config(bg = color[5],text=puntos[5])
  btn_padrao3x1_6.config(bg = color[6],text=puntos[6])
  btn_padrao3x1_7.config(bg = color[7],text=puntos[7])
  btn_padrao3x1_8.config(bg = color[8],text=puntos[8])
  btn_padrao3x1_9.config(bg = color[9],text=puntos[9])
  btn_padrao3x1_10.config(bg = color[10],text=puntos[10])
  btn_padrao3x1_11.config(bg = color[11],text=puntos[11])
  btn_padrao3x1_12.config(bg = color[12],text=puntos[12])
  btn_padrao3x1_13.config(bg = color[13],text=puntos[13])
  btn_padrao3x1_14.config(bg = color[14],text=puntos[14])
  btn_padrao3x1_15.config(bg = color[15],text=puntos[15])
  btn_padrao3x1_16.config(bg = color[16],text=puntos[16])
  btn_padrao3x1_17.config(bg = color[17],text=puntos[17])
  btn_padrao3x1_18.config(bg = color[18],text=puntos[18])
  btn_padrao3x1_19.config(bg = color[19],text=puntos[19])
  btn_padrao3x1_20.config(bg = color[20],text=puntos[20])
  btn_padrao3x1_21.config(bg = color[21],text=puntos[21])
  btn_padrao3x1_22.config(bg = color[22],text=puntos[22])
  btn_padrao3x1_23.config(bg = color[23],text=puntos[23])
  btn_padrao3x1_24.config(bg = color[24],text=puntos[24])
  btn_padrao3x1_25.config(bg = color[25],text=puntos[25])
  btn_padrao3x1_26.config(bg = color[26],text=puntos[26])
  btn_padrao3x1_27.config(bg = color[27],text=puntos[27])
  btn_padrao3x1_28.config(bg = color[28],text=puntos[28])
  btn_padrao3x1_29.config(bg = color[29],text=puntos[29])
  btn_padrao3x1_30.config(bg = color[30],text=puntos[30])
  btn_padrao3x1_31.config(bg = color[31],text=puntos[31])
  btn_padrao3x1_32.config(bg = color[32],text=puntos[32])
  btn_padrao3x1_33.config(bg = color[33],text=puntos[33])
  btn_padrao3x1_34.config(bg = color[34],text=puntos[34])
  btn_padrao3x1_35.config(bg = color[35],text=puntos[35])
  btn_padrao3x1_36.config(bg = color[36],text=puntos[36])
  btn_padrao3x1_37.config(bg = color[37],text=puntos[37])
  btn_padrao3x1_38.config(bg = color[38],text=puntos[38])
  btn_padrao3x1_39.config(bg = color[39],text=puntos[39])
  
  btn_cata_img12.config(image=seleccionar_foto(divisa))
  
  lbl_porciento12.config(text = "{0:.1f}".format(porciento_final) + " %",fg = fg_porciento)
  lbl_cata_divisa12.config(text = divisa)   
  global win_12
  global hit_12
  global g1_12
  global g2_12
  global g3_12
  global g4_12
  global g5_12
  n = 0
  win_12 = 0
  hit_12 = 0
  g1_12 = 0
  g2_12 = 0
  g3_12 = 0
  g4_12 = 0
  g5_12 = 0
  while n < 40:
       if puntos[n] == "G1":
         win_12 = win_12 + 1
       if puntos[n] == "G1":
         g1_12 = g1_12 + 1
       if puntos[n] == "G2":
         g2_12 = g2_12 + 1
       if puntos[n] == "G3":
         g3_12 = g3_12 + 1  
       if puntos[n] == "G4":
         g4_12 = g4_12 + 1
       if puntos[n] == "G5":
         g5_12 = g5_12 + 1
       n = n + 1  
  g1_12st = str(g1_12)
  g2_12st = str(g2_12)
  g3_12st = str(g3_12)
  g4_12st = str(g4_12)
  g5_12st = str(g5_12)
  win_12 = round(((porciento_final / 100) * 40)- (g1_12 + g2_12 + g3_12 + g4_12 + g5_12)) 
  hit_12 = (40 - (win_12 + g1_12 + g2_12 + g3_12 + g4_12 + g5_12))
  win_12st = str(win_12)
  hit_12st = str(hit_12)
  if martin_gala == 0:
    lbl_estadisticas_win_12.config(text = "Win: " + win_12st)
    lbl_estadisticas_hit_12.config(text = "Hit: " + hit_12st)
    lbl_estadisticas_g1_12.config(text = "")
    lbl_estadisticas_g2_12.config(text = "")
    lbl_estadisticas_g3_12.config(text = "")
    lbl_estadisticas_g4_12.config(text = "")
    lbl_estadisticas_g5_12.config(text = "")
    
  if martin_gala == 1:
    lbl_estadisticas_win_12.config(text = "Win: " + win_12st)
    lbl_estadisticas_hit_12.config(text = "Hit: " + hit_12st)
    lbl_estadisticas_g1_12.config(text = "G1\n" + g1_12st)
    lbl_estadisticas_g2_12.config(text = "")
    lbl_estadisticas_g3_12.config(text = "")
    lbl_estadisticas_g4_12.config(text = "")
    lbl_estadisticas_g5_12.config(text = "")
       
  if martin_gala == 2:
    lbl_estadisticas_win_12.config(text = "Win: " + win_12st)
    lbl_estadisticas_hit_12.config(text = "Hit: " + hit_12st)       
    lbl_estadisticas_g1_12.config(text = "G1\n" + g1_12st)
    lbl_estadisticas_g2_12.config(text = "G2\n" + g2_12st)
    lbl_estadisticas_g3_12.config(text = "")
    lbl_estadisticas_g4_12.config(text = "")
    lbl_estadisticas_g5_12.config(text = "")
    
  if martin_gala == 3:
    lbl_estadisticas_win_12.config(text = "Win: " + win_12st)
    lbl_estadisticas_hit_12.config(text = "Hit: " + hit_12st)  
    lbl_estadisticas_g1_12.config(text = "G1\n" + g1_12st)
    lbl_estadisticas_g2_12.config(text = "G2\n" + g2_12st)
    lbl_estadisticas_g3_12.config(text = "G3\n" + g3_12st) 
    lbl_estadisticas_g4_12.config(text = "")
    lbl_estadisticas_g5_12.config(text = "")
    
  if martin_gala == 4:
    lbl_estadisticas_win_12.config(text = "Win: " + win_12st)
    lbl_estadisticas_hit_12.config(text = "Hit: " + hit_12st)  
    lbl_estadisticas_g1_12.config(text = "G1\n" + g1_12st)
    lbl_estadisticas_g2_12.config(text = "G2\n" + g2_12st)
    lbl_estadisticas_g3_12.config(text = "G3\n" + g3_12st)
    lbl_estadisticas_g4_12.config(text = "G4\n" + g4_12st)
    lbl_estadisticas_g5_12.config(text = "")
    
  if martin_gala == 5:
    lbl_estadisticas_win_12.config(text = "Win: " + win_12st)
    lbl_estadisticas_hit_12.config(text = "Hit: " + hit_12st)  
    lbl_estadisticas_g1_12.config(text = "G1\n" + g1_12st)
    lbl_estadisticas_g2_12.config(text = "G2\n" + g2_12st)
    lbl_estadisticas_g3_12.config(text = "G3\n" + g3_12st)
    lbl_estadisticas_g4_12.config(text = "G4\n" + g4_12st)
    lbl_estadisticas_g5_12.config(text = "G5\n" + g5_12st)
    
def estadisticas_totales(martin_gala):
    global win_1
    global hit_1
    global g1_1
    global g2_1
    global g3_1
    global g4_1
    global g5_1
    global win_2
    global hit_2
    global g1_2
    global g2_2
    global g3_2
    global g4_2
    global g5_2
    global win_3
    global hit_3
    global g1_3
    global g2_3
    global g3_3
    global g4_3
    global g5_3
    global win_4
    global hit_4
    global g1_4
    global g2_4
    global g3_4
    global g4_4
    global g5_4
    global win_5
    global hit_5
    global g1_5
    global g2_5
    global g3_5
    global g4_5
    global g5_5
    global win_6
    global hit_6
    global g1_6
    global g2_6
    global g3_6
    global g4_6
    global g5_6
    global win_7
    global hit_7
    global g1_7
    global g2_7
    global g3_7
    global g4_7
    global g5_7
    global win_8
    global hit_8
    global g1_8
    global g2_8
    global g3_8
    global g4_8
    global g5_8
    global win_9
    global hit_9
    global g1_9
    global g2_9
    global g3_9
    global g4_9
    global g5_9
    global win_10
    global hit_10
    global g1_10
    global g2_10
    global g3_10
    global g4_10
    global g5_10
    global win_11
    global hit_11
    global g1_11
    global g2_11
    global g3_11
    global g4_11
    global g5_11
    global win_12
    global hit_12
    global g1_12
    global g2_12
    global g3_12
    global g4_12
    global g5_12
    
    win_total_str = str(win_1 + win_2 + win_3 + win_4 + win_5 + win_6 + win_7 + win_8 + win_9 + win_10 + win_11 + win_12)
    g1_total_str = str(g1_1 + g1_2 + g1_3 + g1_4 + g1_5 + g1_6 + g1_7 + g1_8 + g1_9 + g1_10 + g1_11 + g1_12)
    g2_total_str = str(g2_1 + g2_2 + g2_3 + g2_4 + g2_5 + g2_6 + g2_7 + g2_8 + g2_9 + g2_10 + g2_11 + g2_12)
    g3_total_str = str(g3_1 + g3_2 + g3_3 + g3_4 + g3_5 + g3_6 + g3_7 + g3_8 + g3_9 + g3_10 + g3_11 + g3_12)
    g4_total_str = str(g4_1 + g4_2 + g4_3 + g4_4 + g4_5 + g4_6 + g4_7 + g4_8 + g4_9 + g4_10 + g4_11 + g4_12)
    g5_total_str = str(g5_1 + g5_2 + g5_3 + g5_4 + g5_5 + g5_6 + g5_7 + g5_8 + g5_9 + g5_10 + g5_11 + g5_12)
    hit_total_str = str(hit_1 + hit_2 + hit_3 + hit_4 + hit_5 + hit_6 + hit_7 + hit_8 + hit_9 + hit_10 + hit_11 + hit_12)
    hora_actual = str(datetime.now())
    lbl_estadisticas_hora.config(text = "Ultima actualización: " + hora_actual, fg = "white")
    
    if martin_gala == "MG0":
     lbl_estadisticas_win_total.config(text = "Totales=  Win: " + win_total_str, fg = "white")
     lbl_estadisticas_uno_total.config(text = "Hit: " + hit_total_str, fg = "indianred2")
     lbl_estadisticas_dos_total.config(text = "")
     lbl_estadisticas_tres_total.config(text = "")
     lbl_estadisticas_cuatro_total.config(text = "")
     lbl_estadisticas_cinco_total.config(text = "")
     lbl_estadisticas_seis_total.config(text = "")
     
    if martin_gala == "MG1":
     lbl_estadisticas_win_total.config(text = "Totales=  Win: " + win_total_str, fg = "white")
     lbl_estadisticas_uno_total.config(text = "G1: " + g1_total_str, fg = "white")
     lbl_estadisticas_dos_total.config(text = "Hit: " + hit_total_str, fg = "indianred2")
     lbl_estadisticas_tres_total.config(text = "")
     lbl_estadisticas_cuatro_total.config(text = "")
     lbl_estadisticas_cinco_total.config(text = "")
     lbl_estadisticas_seis_total.config(text = "")
        
    if martin_gala == "MG2":
     lbl_estadisticas_win_total.config(text = "Totales=  Win: " + win_total_str, fg = "white")
     lbl_estadisticas_uno_total.config(text = "G1: " + g1_total_str, fg = "white")
     lbl_estadisticas_dos_total.config(text = "G2: " + g2_total_str, fg = "white")
     lbl_estadisticas_tres_total.config(text = "Hit: " + hit_total_str, fg = "indianred2")
     lbl_estadisticas_cuatro_total.config(text = "")
     lbl_estadisticas_cinco_total.config(text = "")
     lbl_estadisticas_seis_total.config(text = "")
     
    if martin_gala == "MG3":
     lbl_estadisticas_win_total.config(text = "Totales=  Win: " + win_total_str, fg = "white")
     lbl_estadisticas_uno_total.config(text = "G1: " + g1_total_str, fg = "white")
     lbl_estadisticas_dos_total.config(text = "G2: " + g2_total_str, fg = "white")
     lbl_estadisticas_tres_total.config(text = "G3: " + g3_total_str, fg = "white")
     lbl_estadisticas_cuatro_total.config(text = "Hit: " + hit_total_str, fg = "indianred2")
     lbl_estadisticas_cinco_total.config(text = "")
     lbl_estadisticas_seis_total.config(text = "")
     
    if martin_gala == "MG4":
     lbl_estadisticas_win_total.config(text = "Totales=  Win: " + win_total_str, fg = "white")
     lbl_estadisticas_uno_total.config(text = "G1: " + g1_total_str, fg = "white")
     lbl_estadisticas_dos_total.config(text = "G2: " + g2_total_str, fg = "white")
     lbl_estadisticas_tres_total.config(text = "G3: " + g3_total_str, fg = "white")
     lbl_estadisticas_cuatro_total.config(text = "G4: " + g4_total_str, fg = "white")
     lbl_estadisticas_cinco_total.config(text = "Hit: " + hit_total_str, fg = "indianred2")
     lbl_estadisticas_seis_total.config(text = "")
     
    if martin_gala == "MG5":
     lbl_estadisticas_win_total.config(text = "Totales=  Win: " + win_total_str, fg = "white")
     lbl_estadisticas_uno_total.config(text = "G1: " + g1_total_str, fg = "white")
     lbl_estadisticas_dos_total.config(text = "G2: " + g2_total_str, fg = "white")
     lbl_estadisticas_tres_total.config(text = "G3: " + g3_total_str, fg = "white")
     lbl_estadisticas_cuatro_total.config(text = "G4: " + g4_total_str, fg = "white")
     lbl_estadisticas_cinco_total.config(text = "G5: " + g5_total_str, fg = "white")
     lbl_estadisticas_seis_total.config(text = "Hit: " + hit_total_str, fg = "indianred2") 
    
     
###################################MODO CONEXION##################################    
btn_real = Button(borderwidth = 0,bg = "white",text="REAL",width = 10, command=lambda:[app.after(200,balance,"REAL"),botones_modo(0)])
btn_real.place(x=1185, y=154)  

btn_practice = Button(borderwidth = 0,bg = "gray", text= "PRACTICE",width = 10, command=lambda:[app.after(200,balance,"PRACTICE"),botones_modo(1)])
btn_practice.place(x=1260, y=154)     

 
def botones_modo(modo_boton):
    global modo_cuenta
    if modo_boton == 0:
        modo_cuenta = "REAL"
        btn_real.config(bg="white")
        btn_practice.config(bg="gray")
        combo_mode_label_p1.config(text="REAL", fg = "Spring green")
        combo_mode_label_p2.config(text="REAL", fg = "Spring green")
        combo_mode_label_p3.config(text="REAL", fg = "Spring green")
        combo_mode_label_p4.config(text="REAL", fg = "Spring green")
        
    if modo_boton == 1:
        modo_cuenta = "PRACTICE"
        btn_practice.config(bg="white")
        btn_real.config(bg="gray")
        combo_mode_label_p1.config(text="PRACTICE", fg = color_mamey)
        combo_mode_label_p2.config(text="PRACTICE", fg = color_mamey)
        combo_mode_label_p3.config(text="PRACTICE", fg = color_mamey)
        combo_mode_label_p4.config(text="PRACTICE", fg = color_mamey)
       
################################BALANCE GRAFICO###################################

lbl_banca = Label(text = "0.00", bg = color_fondo, fg = "spring green")
lbl_banca.place(x=1225, y=90)
lbl_banca.config(font=('Arial',20))

def balance_real(monto,modo):
 if modo == "REAL":
  lbl_banca.config(text=monto, fg = "spring green")
 if modo == "PRACTICE":
  lbl_banca.config(text=monto, fg = color_mamey)
#################################PORCENTAJE GANADAS#############################
mas_win = Label(text = "+00", bg = color_fondo, fg = "spring green")
mas_win.place(x=1190, y=126)
mas_win.config(font=('Arial',7))

menos_loss = Label(text = "-00", bg = color_fondo, fg = "firebrick2")
menos_loss.place(x=1250, y=126)
menos_loss.config(font=('Arial',7))

mas_menos = Label(text = "$00", bg = color_fondo, fg = "white")
mas_menos.place(x=1307, y=126)
mas_menos.config(font=('Arial',7))

resultado_win2 = 0.0
resultado_loss2 = 0.0

def ganancias_totales(envios):
   
    if envios > 0:
     resultado_win = envios 
     global resultado_win2
     resultado_win2 = resultado_win2 + resultado_win
    
    if envios < 0:
     resultado_loss = envios 
     global resultado_loss2
     resultado_loss2 = resultado_loss2 + resultado_loss
     
    mas_win.config(text="+" + "{:.2f}".format(resultado_win2))
     
    menos_loss.config(text="-" + "{:.2f}".format(resultado_loss2))
    global t_final
    t_final = resultado_win2 + resultado_loss2

    
    if t_final >= 0:
     mas_menos.config(text="$+" + "{:.2f}".format(t_final), fg="spring green")
     
    if t_final < 0:
     mas_menos.config(text="$-" + "{:.2f}".format(t_final), fg="firebrick2")
    
    
################################GLOBAL GRAFICOS#################################

lbl_win_total = Label(text = "00", bg =color_fondo3, fg = "black")
lbl_win_total.place(x=1192, y=236)
lbl_win_total.config(font=('Arial',32))
  
lbl_loose_total = Label(text = "00", bg =color_fondo3, fg = "black")
lbl_loose_total.place(x=1283, y=236)
lbl_loose_total.config(font=('Arial',32))


def graf_global():
 global status_p1_win 
 global status_p1_loose 
 global status_p2_win 
 global status_p2_loose 
 global status_p3_win 
 global status_p3_loose 
 global status_p4_win 
 global status_p4_loose 
 global status_p5_win 
 global status_p5_loose 
 global status_global_win2 
 global status_global_loose2
 
 status_global_win = status_p1_win +  status_p2_win +  status_p3_win +  status_p4_win +  status_p5_win 
 status_global_loose = status_p1_loose + status_p2_loose + status_p3_loose + status_p4_loose + status_p5_loose 

 status_global_win2 = str(status_global_win) 
 if status_global_win < 10:  
  lbl_win_total.config(text = "0" + status_global_win2)
 else:
  lbl_win_total.config(text = status_global_win2)
  
 status_global_loose2 = str(status_global_loose) 
 if status_global_loose < 10: 
  lbl_loose_total.config(text = "0" + status_global_loose2)
 else:
  lbl_loose_total.config(text = status_global_loose2)
  
 if status_global_loose > 99 and status_global_loose < 1000: 
  lbl_loose_total.config(font=('Arial',22))
  lbl_loose_total.place(x=1283, y=243)
  
 if status_global_loose > 999: 
  lbl_loose_total.config(font=('Arial',18))
  lbl_loose_total.place(x=1281, y=248)
  
 if status_global_win > 99 and status_global_win < 1000: 
  lbl_win_total.config(font=('Arial',22))
  lbl_win_total.place(x=1192, y=243)
  
 if status_global_win > 999: 
  lbl_win_total.config(font=('Arial',18))
  lbl_win_total.place(x=1190, y=248)
#############################PANEL 1 GRAFICOS#########################################

notificacion_p1 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_p1.place(x=155, y=297)
notificacion_p1.config(font=('Arial',7))

notificacion_remaning_p1 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_remaning_p1.place(x=255, y=297)
notificacion_remaning_p1.config(font=('Arial',7))


lbl_win_p1 = Label(text="00", bg =color_fondo3, fg = "darkgreen")
lbl_win_p1.place(x=210, y=279)
lbl_win_p1.config(font=('Arial',7)) 

lbl_loose_p1 = Label(text="00", bg =color_fondo3, fg = "firebrick2")
lbl_loose_p1.place(x=257, y=279)
lbl_loose_p1.config(font=('Arial',7))

lbl_seg_p1 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_seg_p1.place(x=169, y=279)
lbl_seg_p1.config(font=('Arial',7)) 

lbl_minu_p1 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_minu_p1.place(x=152, y=279)
lbl_minu_p1.config(font=('Arial',7))

lbl_hora_p1 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_hora_p1.place(x=135, y=279)
lbl_hora_p1.config(font=('Arial',7))

#############################PANEL 2 GRAFICOS#########################################

notificacion_p2 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_p2.place(x=155+209, y=297)
notificacion_p2.config(font=('Arial',7))

notificacion_remaning_p2 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_remaning_p2.place(x=255+209, y=297)
notificacion_remaning_p2.config(font=('Arial',7))


lbl_win_p2 = Label(text="00", bg =color_fondo3, fg = "darkgreen")
lbl_win_p2.place(x=210+209, y=279)
lbl_win_p2.config(font=('Arial',7)) 

lbl_loose_p2 = Label(text="00", bg =color_fondo3, fg = "firebrick2")
lbl_loose_p2.place(x=257+209, y=279)
lbl_loose_p2.config(font=('Arial',7))

lbl_seg_p2 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_seg_p2.place(x=169+209, y=279)
lbl_seg_p2.config(font=('Arial',7)) 

lbl_minu_p2 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_minu_p2.place(x=152+209, y=279)
lbl_minu_p2.config(font=('Arial',7))

lbl_hora_p2 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_hora_p2.place(x=135+209, y=279)
lbl_hora_p2.config(font=('Arial',7)) 

#############################PANEL 3 GRAFICOS#########################################

notificacion_p3 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_p3.place(x=155+418, y=297)
notificacion_p3.config(font=('Arial',7))

notificacion_remaning_p3 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_remaning_p3.place(x=255+418, y=297)
notificacion_remaning_p3.config(font=('Arial',7))


lbl_win_p3 = Label(text="00", bg =color_fondo3, fg = "darkgreen")
lbl_win_p3.place(x=210+418, y=279)
lbl_win_p3.config(font=('Arial',7)) 

lbl_loose_p3 = Label(text="00", bg =color_fondo3, fg = "firebrick2")
lbl_loose_p3.place(x=257+418, y=279)
lbl_loose_p3.config(font=('Arial',7))

lbl_seg_p3 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_seg_p3.place(x=169+418, y=279)
lbl_seg_p3.config(font=('Arial',7)) 

lbl_minu_p3 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_minu_p3.place(x=152+418, y=279)
lbl_minu_p3.config(font=('Arial',7))

lbl_hora_p3 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_hora_p3.place(x=135+418, y=279)
lbl_hora_p3.config(font=('Arial',7))

#############################PANEL 4 GRAFICOS#########################################

notificacion_p4 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_p4.place(x=155+627, y=297)
notificacion_p4.config(font=('Arial',7))

notificacion_remaning_p4 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_remaning_p4.place(x=255+627, y=297)
notificacion_remaning_p4.config(font=('Arial',7))

lbl_win_p4 = Label(text="00", bg =color_fondo3, fg = "darkgreen")
lbl_win_p4.place(x=210+627, y=279)
lbl_win_p4.config(font=('Arial',7)) 

lbl_loose_p4 = Label(text="00", bg =color_fondo3, fg = "firebrick2")
lbl_loose_p4.place(x=257+627, y=279)
lbl_loose_p4.config(font=('Arial',7))

lbl_seg_p4 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_seg_p4.place(x=169+627, y=279)
lbl_seg_p4.config(font=('Arial',7)) 

lbl_minu_p4 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_minu_p4.place(x=152+627, y=279)
lbl_minu_p4.config(font=('Arial',7))

lbl_hora_p4 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_hora_p4.place(x=135+627, y=279)
lbl_hora_p4.config(font=('Arial',7))

#############################PANEL 5 GRAFICOS#########################################

notificacion_p5 = Label(text= "", bg =color_fondo, fg = "white")
notificacion_p5.place(x=155+835, y=297)
notificacion_p5.config(font=('Arial',7))

lbl_win_p5 = Label(text="00", bg =color_fondo3, fg = "darkgreen")
lbl_win_p5.place(x=210+841, y=279)
lbl_win_p5.config(font=('Arial',7)) 

lbl_loose_p5 = Label(text="00", bg =color_fondo3, fg = "firebrick2")
lbl_loose_p5.place(x=257+841, y=279)
lbl_loose_p5.config(font=('Arial',7))

lbl_seg_p5 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_seg_p5.place(x=169+841, y=279)
lbl_seg_p5.config(font=('Arial',7)) 

lbl_minu_p5 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_minu_p5.place(x=152+841, y=279)
lbl_minu_p5.config(font=('Arial',7))

lbl_hora_p5 = Label(text="00", bg =color_fondo3, fg = "black")
lbl_hora_p5.place(x=135+841, y=279)
lbl_hora_p5.config(font=('Arial',7)) 

def start_time_remaning_p1():
    time_remaning_hilo = threading.Thread(target=time_remaning_p1())
    time_remaning_hilo.start()
def start_time_remaning_p2():
    time_remaning_hilo2 = threading.Thread(target=time_remaning_p2())
    time_remaning_hilo2.start()
def start_time_remaning_p3():
    time_remaning_hilo3 = threading.Thread(target=time_remaning_p3())
    time_remaning_hilo3.start()
def start_time_remaning_p4():
    time_remaning_hilo4 = threading.Thread(target=time_remaning_p4())
    time_remaning_hilo4.start()
    
def time_remaning_p1():
    while True:
     remaning = datetime.now()
     seg_remaning = format(remaning.second)
     seg_remaning2 = int(seg_remaning)
     seg_remaning3 = (seg_remaning2 - 60) * -1
     seg_remaning3 = str(seg_remaning3)
     
     if seg_remaning2 <= 50:
      notificacion_remaning_p1.config(text= "⏰ " + seg_remaning3)
     if seg_remaning2 >= 51:
      notificacion_remaning_p1.config(text= "⏰ " + "0"+seg_remaning3)
     time.sleep(1)
     
     if seg_remaning == "59":
         notificacion_remaning_p1.config(text= "⏰ " + "00")
         time.sleep(1)
         notificacion_remaning_p1.config(text="")
         break
 
def time_remaning_p2():
    while True:
     remaning = datetime.now()
     seg_remaning = format(remaning.second)
     seg_remaning2 = int(seg_remaning)
     seg_remaning3 = (seg_remaning2 - 60) * -1
     seg_remaning3 = str(seg_remaning3)
     
     if seg_remaning2 <= 50:
      notificacion_remaning_p2.config(text= "⏰ " + seg_remaning3)
     if seg_remaning2 >= 51:
      notificacion_remaning_p2.config(text= "⏰ " + "0"+seg_remaning3)
     time.sleep(1)
     
     if seg_remaning == "59":
         notificacion_remaning_p2.config(text= "⏰ " + "00")
         time.sleep(1)
         notificacion_remaning_p2.config(text="")
         break  
def time_remaning_p3():
    while True:
     remaning = datetime.now()
     seg_remaning = format(remaning.second)
     seg_remaning2 = int(seg_remaning)
     seg_remaning3 = (seg_remaning2 - 60) * -1
     seg_remaning3 = str(seg_remaning3)
     
     if seg_remaning2 <= 50:
      notificacion_remaning_p3.config(text= "⏰ " + seg_remaning3)
     if seg_remaning2 >= 51:
      notificacion_remaning_p3.config(text= "⏰ " + "0"+seg_remaning3)
     time.sleep(1)
     
     if seg_remaning == "59":
         notificacion_remaning_p3.config(text= "⏰ " + "00")
         time.sleep(1)
         notificacion_remaning_p3.config(text="")
         break 
        
def time_remaning_p4():
    while True:
     remaning = datetime.now()
     seg_remaning = format(remaning.second)
     seg_remaning2 = int(seg_remaning)
     seg_remaning3 = (seg_remaning2 - 60) * -1
     seg_remaning3 = str(seg_remaning3)
     
     if seg_remaning2 <= 50:
      notificacion_remaning_p4.config(text= "⏰ " + seg_remaning3)
     if seg_remaning2 >= 51:
      notificacion_remaning_p4.config(text= "⏰ " + "0"+seg_remaning3)
     time.sleep(1)
     
     if seg_remaning == "59":
         notificacion_remaning_p4.config(text= "⏰ " + "00")
         time.sleep(1)
         notificacion_remaning_p4.config(text="")
         break 



def graf_panel1(notificacion1):   
 notificacion_p1.config(text = notificacion1)
 if notificacion1 == "Operacion Terminada" or notificacion1 == "Stop Ops ON" or notificacion1 == "Stop Gain ON" or notificacion1 == "Stop Loss ON" or notificacion1 == "Tiempo Terminado" or notificacion1 == "Error en operacion":
  stop_time_p1("stop")
  start_panel1.config(state="normal")
  
def graf_panel2(notificacion2):   
 notificacion_p2.config(text = notificacion2)
 if notificacion2 == "Operacion Terminada" or notificacion2 == "Stop Ops ON" or notificacion2 == "Stop Gain ON" or notificacion2 == "Stop Loss ON" or notificacion2 == "Tiempo Terminado" or notificacion2 == "Error en operacion":
  stop_time_p2("stop")
  start_panel2.config(state="normal")
  
def graf_panel3(notificacion3): 
 notificacion_p3.config(text = notificacion3)
 if notificacion3 == "Operacion Terminada" or notificacion3 == "Stop Ops ON" or notificacion3 == "Stop Gain ON" or notificacion3 == "Stop Loss ON" or notificacion3 == "Tiempo Terminado" or notificacion3 == "Error en operacion":
  stop_time_p3("stop")
  start_panel3.config(state="normal")
  
def graf_panel4(notificacion4):   
 notificacion_p4.config(text = notificacion4)
 if notificacion4 == "Operacion Terminada" or notificacion4 == "Stop Ops ON" or notificacion4 == "Stop Gain ON" or notificacion4 == "Stop Loss ON" or notificacion4 == "Tiempo Terminado" or notificacion4 == "Error en operacion":
  stop_time_p4("stop")
  start_panel4.config(state="normal")
  
def graf_panel5(notificacion5):  
 notificacion_p5.config(text = notificacion5)
 if notificacion5 == "Operacion Terminada" or notificacion5 == "Stop Ops ON" or notificacion5 == "Stop Gain ON" or notificacion5 == "Stop Loss ON" or notificacion5 == "Tiempo Terminado" or notificacion5 == "Error en operacion":
  stop_time_p5("stop")
  start_panel5.config(state="normal")
  
####################################### RESET ##########################################################

def reset_todo():
 lbl_seg_p1.config(text= "00")
 lbl_seg_p2.config(text= "00")
 lbl_seg_p3.config(text= "00")
 lbl_seg_p4.config(text= "00")
 lbl_seg_p5.config(text= "00")
 lbl_minu_p1.config(text= "00")
 lbl_minu_p2.config(text= "00")
 lbl_minu_p3.config(text= "00")
 lbl_minu_p4.config(text= "00")
 lbl_minu_p5.config(text= "00")
 lbl_hora_p1.config(text= "00")
 lbl_hora_p2.config(text= "00")
 lbl_hora_p3.config(text= "00")
 lbl_hora_p4.config(text= "00")
 lbl_hora_p5.config(text= "00")
 #___________________________________________________-
 lbl_win_p1.config(text = "00") 
 lbl_win_p2.config(text = "00")
 lbl_win_p3.config(text = "00")
 lbl_win_p4.config(text = "00")
 lbl_win_p5.config(text = "00")
 lbl_loose_p1.config(text = "00") 
 lbl_loose_p2.config(text = "00")
 lbl_loose_p3.config(text = "00")
 lbl_loose_p4.config(text = "00")
 lbl_loose_p5.config(text = "00") 
 global ganadas_turbo 
 global perdidas_turbo
 ganadas_turbo = 0
 perdidas_turbo = 0 
  
  
def graf_panel1_time(seg,minu,hora):
 
  
 seg2 = str(seg)
 minu2 = str(minu)
 hora2 = str(hora)  
 
 if  seg <= 9:
  lbl_seg_p1.config(text='0' + seg2)
 else:
  lbl_seg_p1.config(text=seg2)
  
 if  minu <= 9:
  lbl_minu_p1.config(text='0' + minu2+':')
 if  minu >= 10:
  lbl_minu_p1.config(text=minu2+':')
 
 if  hora <= 9:
  lbl_hora_p1.config(text='0' + hora2+':')
 if  hora >= 10:   
  lbl_hora_p1.config(text=hora2+':')
  
def graf_panel2_time(seg,minu,hora):
 
  
 seg2 = str(seg)
 minu2 = str(minu)
 hora2 = str(hora)  
 
 if  seg <= 9:
  lbl_seg_p2.config(text='0' + seg2)
 else:
  lbl_seg_p2.config(text=seg2)
  
 if  minu <= 9:
  lbl_minu_p2.config(text='0' + minu2+':')
 if  minu >= 10:
  lbl_minu_p2.config(text=minu2+':')
 
 if  hora <= 9:
  lbl_hora_p2.config(text='0' + hora2+':')
 if  hora >= 10:   
  lbl_hora_p2.config(text=hora2+':')
 
def graf_panel3_time(seg,minu,hora):
 
  
 seg2 = str(seg)
 minu2 = str(minu)
 hora2 = str(hora)  
 
 if  seg <= 9:
  lbl_seg_p3.config(text='0' + seg2)
 else:
  lbl_seg_p3.config(text=seg2)
  
 if  minu <= 9:
  lbl_minu_p3.config(text='0' + minu2+':')
 if  minu >= 10:
  lbl_minu_p3.config(text=minu2+':')
 
 if  hora <= 9:
  lbl_hora_p3.config(text='0' + hora2+':')
 if  hora >= 10:   
  lbl_hora_p3.config(text=hora2+':')
  
def graf_panel4_time(seg,minu,hora):
  
 seg2 = str(seg)
 minu2 = str(minu)
 hora2 = str(hora)  
 
 if  seg <= 9:
  lbl_seg_p4.config(text='0' + seg2)
 else:
  lbl_seg_p4.config(text=seg2)
  
 if  minu <= 9:
  lbl_minu_p4.config(text='0' + minu2+':')
 if  minu >= 10:
  lbl_minu_p4.config(text=minu2+':')
 
 if  hora <= 9:
  lbl_hora_p4.config(text='0' + hora2+':')
 if  hora >= 10:   
  lbl_hora_p4.config(text=hora2+':')  
  
  
def graf_panel5_time(seg,minu,hora):
    try:
     global minu_5
     global hora_5
     minu_5 = minu
     hora_5 = hora
      
     seg2 = str(seg)
     minu2 = str(minu)
     hora2 = str(hora)  
     
     if  seg <= 9:
      lbl_seg_p5.config(text='0' + seg2)
     else:
      lbl_seg_p5.config(text=seg2)
      
     if  minu <= 9:
      lbl_minu_p5.config(text='0' + minu2+':')
     if  minu >= 10:
      lbl_minu_p5.config(text=minu2+':')
     
     if  hora <= 9:
      lbl_hora_p5.config(text='0' + hora2+':')
     if  hora >= 10:   
      lbl_hora_p5.config(text=hora2+':')
    except: print("Label error")
 
def graf_panel1_score(status_p1_win2,status_p1_loose2):
 global status_p1_win 
 global status_p1_loose 
 status_p1_win = status_p1_win2
 status_p1_loose = status_p1_loose2
 status_p1_win2 = str(status_p1_win)
 status_p1_loose2 = str(status_p1_loose)
 
 if status_p1_win < 10:
  lbl_win_p1.config(text = "0" + status_p1_win2)
 else:
  lbl_win_p1.config(text = status_p1_win2)
  
 if status_p1_loose < 10: 
  lbl_loose_p1.config(text = "0" + status_p1_loose2)
 else:
  lbl_loose_p1.config(text = status_p1_loose2)
  
def graf_panel2_score(status_p2_win2,status_p2_loose2):
 global status_p2_win 
 global status_p2_loose 
 status_p2_win = status_p2_win2
 status_p2_loose = status_p2_loose2
  
 status_p2_win2 = str(status_p2_win)
 status_p2_loose2 = str(status_p2_loose)
 
 if status_p2_win < 10:
  lbl_win_p2.config(text = "0" + status_p2_win2)
 else:
  lbl_win_p2.config(text = status_p2_win2)
  
 if status_p2_loose < 10: 
  lbl_loose_p2.config(text = "0" + status_p2_loose2)
 else:
  lbl_loose_p2.config(text = status_p2_loose2)
  
def graf_panel3_score(status_p3_win2,status_p3_loose2):
 global status_p3_win 
 global status_p3_loose
 status_p3_win = status_p3_win2
 status_p3_loose = status_p3_loose2
  
 status_p3_win2 = str(status_p3_win)
 status_p3_loose2 = str(status_p3_loose)
 
 if status_p3_win < 10:
  lbl_win_p3.config(text = "0" + status_p3_win2)
 else:
  lbl_win_p3.config(text = status_p3_win2)
  
 if status_p3_loose < 10: 
  lbl_loose_p3.config(text = "0" + status_p3_loose2)
 else:
  lbl_loose_p3.config(text = status_p3_loose2)
  
def graf_panel4_score(status_p4_win2,status_p4_loose2):
 global status_p4_win 
 global status_p4_loose 
 status_p4_win = status_p4_win2
 status_p4_loose = status_p4_loose2
 
 status_p4_win2 = str(status_p4_win)
 status_p4_loose2 = str(status_p4_loose)
 
 if status_p4_win < 10:
  lbl_win_p4.config(text = "0" + status_p4_win2)
 else:
  lbl_win_p4.config(text = status_p4_win2)
  
 if status_p4_loose < 10: 
  lbl_loose_p4.config(text = "0" + status_p4_loose2)
 else:
  lbl_loose_p4.config(text = status_p4_loose2)

def graf_panel5_score(status_p5_win2,status_p5_loose2):
 global status_p5_win 
 global status_p5_loose 
 status_p5_win = status_p5_win2
 status_p5_loose = status_p5_loose2 
 status_p5_win2 = str(status_p5_win)
 status_p5_loose2 = str(status_p5_loose)
 
 if status_p5_win < 10:
  lbl_win_p5.config(text = "0" + status_p5_win2)
 else:
  lbl_win_p5.config(text = status_p5_win2)
  
 if status_p5_loose < 10: 
  lbl_loose_p5.config(text = "0" + status_p5_loose2)
 else:
  lbl_loose_p5.config(text = status_p5_loose2)
  
def start_balance():   
  hilo_balance = threading.Thread(target=start_balance2)
  hilo_balance.start()  

  
def start_balance2():
  global modo_cuenta  
  while True:
    balance(modo_cuenta) 
    time.sleep(60)
  
def procesos_automaticos():
  conteo = 0  
  while True:
   global divisa
   global divisa_default   
   assets_hilo = threading.Thread(target=status_assets_start)
   assets_hilo.start()  
   assets_hilo.join() 
   time.sleep(0.2)
   while True:
      if divisa[0] != "assets":
          break
      time.sleep(0.2)
   if conteo == 0:   
    divisa_default = divisa[0] 
   now = datetime.now()
   seg = format(now.second)
   if seg == "0" or seg == "1" or seg == "2":
       time.sleep(5) 
   cata_hilo = threading.Thread(target= llamar_velas, args= (combo_tipo_martin.get(),divisa_default))
   cata_hilo.start()
   
   enviar_profit_p1()
   enviar_profit_p2()
   enviar_profit_p3()
   enviar_profit_p4()
   enviar_profit_p5()
   
   time.sleep(300)
   conteo = 1
   
   
    
    
    
def start_score_p1():
    
 hilo_time1 = threading.Thread(target=score_p1)  
 hilo_time1.start()
 
def start_score_p2():
    
 hilo_time2 = threading.Thread(target=score_p2)  
 hilo_time2.start()
 
def start_score_p3():
    
 hilo_time3 = threading.Thread(target=score_p3)  
 hilo_time3.start()
 
def start_score_p4():
    
 hilo_time4 = threading.Thread(target=score_p4)  
 hilo_time4.start()
 
def start_score_p5():
    
 hilo_time5 = threading.Thread(target=score_p5)  
 hilo_time5.start()
 
def status_assets_start():
 global nombre
 global descripcion
 global comision
 global i 
 nombre = []
 descripcion = []
 comision = []
 
 i = 0
 hilo_status_assets = threading.Thread(target=status_assets)
 hilo_status_assets.start() 

def status_assets():
     def sub_status_assets():
      
      global nombre
      global descripcion
      global comision
      global i 
      while i < 1383:
       if i == 0:
       
         assets2 = api.get_all_init()
         global assets
         assets = assets2["result"]["turbo"]["actives"]  
       i = i + 1  
       x = str(i)
       try:
        estado2 = assets[x]["enabled"]
        expiracion2 = assets[x]["option"]["exp_time"]  
        nombre1 = assets[x]["name"]
        nombre2=nombre1.replace("front.","")
        descripcion1 = assets[x]["description"] 
        descripcion2=descripcion1.replace("front.","")
        descripcion3=descripcion2.replace("(OTC)","")
        comision2 = assets [x]["option"]["profit"]["commission"]
    
        if estado2 == True and expiracion2 == 60:   
         nombre.append(nombre2)
         descripcion.append(descripcion3)
         comision.append(comision2)
       except:
        sub_status_assets()
     sub_status_assets()
     graf_assets(descripcion,comision,nombre)


def stop_time_p1(_stop_time):
    global stop_time_1
    stop_time_1 = _stop_time
def stop_time_p2(_stop_time):
    global stop_time_2
    stop_time_2 = _stop_time
def stop_time_p3(_stop_time):
    global stop_time_3
    stop_time_3 = _stop_time    
def stop_time_p4(_stop_time):
    global stop_time_4
    stop_time_4 = _stop_time
def stop_time_p5(_stop_time):
    global stop_time_5
    stop_time_5 = _stop_time
    
def score_p1(): 
    seg = 0
    minu = 0
    hora = 0
    global stop_time_1
    stop_time_1 = "run"
    
    while True:
      graf_panel1_time(seg,minu,hora)
      seg = seg + 1
      time.sleep(1)
      if seg == 60:
       minu = minu + 1
       seg = 0
      if minu == 60:
       hora = hora + 1
       minu = 0
  
      if stop_time_1 == "stop":
          break
      
def score_p2(): 
    seg = 0
    minu = 0
    hora = 0
    global stop_time_2
    stop_time_2 = "run"
    
    while True:
      graf_panel2_time(seg,minu,hora)
      seg = seg + 1
      time.sleep(1)
      if seg == 60:
       minu = minu + 1
       seg = 0
      if minu == 60:
       hora = hora + 1
       minu = 0
  
      if stop_time_2 == "stop":
          break
      
def score_p3(): 
    seg = 0
    minu = 0
    hora = 0
    global stop_time_3
    stop_time_3 = "run"
    
    while True:
      graf_panel3_time(seg,minu,hora)
      seg = seg + 1
      time.sleep(1)
      if seg == 60:
       minu = minu + 1
       seg = 0
      if minu == 60:
       hora = hora + 1
       minu = 0
  
      if stop_time_3 == "stop":
          break
      
def score_p4(): 
    seg = 0
    minu = 0
    hora = 0
    global stop_time_4
    stop_time_4 = "run"
    
    while True:
      graf_panel4_time(seg,minu,hora)
      seg = seg + 1
      time.sleep(1)
      if seg == 60:
       minu = minu + 1
       seg = 0
      if minu == 60:
       hora = hora + 1
       minu = 0
  
      if stop_time_4 == "stop":
          break
        
        
      
def score_p5(): 
    seg = 0
    minu = 0
    hora = 0
    global stop_time_5
    stop_time_5 = "run"
    
    while True:
      graf_panel5_time(seg,minu,hora)
      seg = seg + 1
      time.sleep(1)
      if seg == 60:
       minu = minu + 1
       seg = 0
      if minu == 60:
       hora = hora + 1
       minu = 0
  
      if stop_time_5 == "stop":
          break
      
balances = ""


def balance(modo_de_operacion):   
     try:
      api.change_balance(modo_de_operacion) 
      balances = api.get_balance()
      balance_real(balances,modo_de_operacion)
     except:
      print ("error al cargar balance")
    
      
      
      
def catalogo_mhi_velas1(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho): 
 #try:
  color_catalogo = ""
  puntos_mg = ""
 
 
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1 
      
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
    vela3 = 1 
  else:
    vela3 = -1
         
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:
    
    if data[cuatro]['open'] < data[cuatro]['close']: 
      vela4 = 1 
    else:
      vela4 = -1 
  
 #______________________________________________________________________     
  if value_mg >= 2:
  
    if data[cinco]['open'] < data[cinco]['close']: 
      vela5 = 1 
    else:
      vela5 = -1 
   
 #__________________________________________________________________
  if value_mg >= 3:
     
    if data[seis]['open'] < data[seis]['close']: 
      vela6 = 1 
    else:
      vela6 = -1 
   
 #_________________________________________________________________
  if value_mg >= 4:

  
    if data[siete]['open'] < data[siete]['close']: 
      vela7 = 1 
    else:
      vela7 = -1 
   
      
  if value_mg >= 5:

  
    if data[ocho]['open'] < data[ocho]['close']: 
      vela8 = 1 
    else:
      vela8 = -1 
   
  #____________________________________________________________________________
  
  mhi = vela0 + vela1 + vela2
  mg = vela3 
 
  if mhi > 0 and mg < 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg > 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela3 != vela4:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela4 != vela5: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela5 != vela6:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela6 != vela7: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela7 != vela8: 
          color_catalogo = "spring green"
          puntos_mg="G5"
  return color_catalogo, puntos_mg     
 #except: print("error1")
  

def catalogo_cuadro1(martingala,divisa,new_data,min_actual):
  #try:
    color = []
    puntos = []
    porciento_green = 0
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 4: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 4: numero_velas = 2 
    
    if numero_velas == 1:
     x = 7
    if numero_velas == 2:
     x = 2
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    
    color = []
    puntos = []   
    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       
       color2, puntos2 = catalogo_mhi_velas1(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    
     
    operacion1(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
     
  #except: print ("error1")      
      
def catalogo_mhi_velas2(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
 
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1

      
 #______________________________________________________________________ 
    
  if value_mg >= 1:
      
   if data[cinco]['open'] < data[cinco]['close']: 
    vela5 = 1 
   else:
    vela5 = -1  
   
    
  if value_mg >= 2:
   
    if data[seis]['open'] < data[seis]['close']: 
      vela6 = 1 
    else:
      vela6 = -1  
   
 #__________________________________________________________________
  if value_mg >= 3:
 
    if data[siete]['open'] < data[siete]['close']: 
      vela7 = 1 
    else:
      vela7 = -1  
   
 #_________________________________________________________________
  if value_mg >= 4:
   
    if data[ocho]['open'] < data[ocho]['close']: 
      vela8 = 1 
    else:
      vela8 = -1  
   

  if value_mg >= 5:
  
    if data[nueve]['open'] < data[nueve]['close']: 
      vela9 = 1 
    else:
      vela9 = -1  
   
   
  #____________________________________________________________________________
  
  
  mhi = vela0 + vela1 + vela2
  mg = vela4 
 
  if mhi > 0 and mg < 0:
    color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg > 0:
    color_catalogo = "spring green" 
   else:      
    color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela4 != vela5:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela5 != vela6: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela6 != vela7:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela7 != vela8: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela8 != vela9: 
          color_catalogo = "spring green"
          puntos_mg="G5" 
  
  return color_catalogo, puntos_mg     
 except:
    print("error2")
  



def catalogo_cuadro2(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 3: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 3: numero_velas = 2 
    
    if numero_velas == 1:
     x = 7
    if numero_velas == 2:
     x = 2
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       
       color2, puntos2 = catalogo_mhi_velas2(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion2(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error2")

def catalogo_mhi_velas3(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
  
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1
 
  if data[cinco]['open'] < data[cinco]['close']: 
    vela5 = 1 
  else:
    vela5 = -1  
      
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:

      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1 
       
 #______________________________________________________________________     
  if value_mg >= 2:
  
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1 
       
  
 #__________________________________________________________________
  if value_mg >= 3:

      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
   
 #_________________________________________________________________
  if value_mg >= 4:

      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  if value_mg >= 5:
    
      if data[diez]['open'] < data[diez]['close']: 
       vela10 = 1 
      else:
       vela10 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0 + vela1 + vela2
  mg = vela5 
 
  if mhi > 0 and mg < 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg > 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela5 != vela6:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela6 != vela7: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela7 != vela8:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela8 != vela9: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela9 != vela10: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
    print("error3")
  


def catalogo_cuadro3(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 2: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 2: numero_velas = 2 
    
    if numero_velas == 1:
     x = 7
    if numero_velas == 2:
     x = 2
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x
    diez2 = 5 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       diez2 = diez2 + 5
       
       color2, puntos2 = catalogo_mhi_velas3(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2,diez2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion3(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error3")

def catalogo_mhi_velas4(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho): 
 try:
  color_catalogo = ""
  puntos_mg = ""
  
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1 
      
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
    vela3 = 1 
  else:
    vela3 = -1
         
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:
    
    if data[cuatro]['open'] < data[cuatro]['close']: 
      vela4 = 1 
    else:
      vela4 = -1 
  
 #______________________________________________________________________     
  if value_mg >= 2:
  
    if data[cinco]['open'] < data[cinco]['close']: 
      vela5 = 1 
    else:
      vela5 = -1 
   
 #__________________________________________________________________
  if value_mg >= 3:
     
    if data[seis]['open'] < data[seis]['close']: 
      vela6 = 1 
    else:
      vela6 = -1 
   
 #_________________________________________________________________
  if value_mg >= 4:

  
    if data[siete]['open'] < data[siete]['close']: 
      vela7 = 1 
    else:
      vela7 = -1 
   
      
  if value_mg >= 5:

  
    if data[ocho]['open'] < data[ocho]['close']: 
      vela8 = 1 
    else:
      vela8 = -1 
   
  #____________________________________________________________________________
  
  mhi = vela0 + vela1 + vela2
  mg = vela3 
 
  if mhi > 0 and mg > 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela3 != vela4:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela4 != vela5: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela5 != vela6:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela6 != vela7: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela7 != vela8: 
          color_catalogo = "spring green"
          puntos_mg="G5"
  return color_catalogo, puntos_mg     
 except: print("error4")
  



def catalogo_cuadro4(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 4: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 4: numero_velas = 2 
    
    if numero_velas == 1:
     x = 7
    if numero_velas == 2:
     x = 2
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       
       color2, puntos2 = catalogo_mhi_velas4(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion4(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error4")    

def catalogo_mhi_velas5(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
  
 
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1

      
 #______________________________________________________________________ 
    
  if value_mg >= 1:
      
   if data[cinco]['open'] < data[cinco]['close']: 
    vela5 = 1 
   else:
    vela5 = -1  
   
    
  if value_mg >= 2:
   
    if data[seis]['open'] < data[seis]['close']: 
      vela6 = 1 
    else:
      vela6 = -1  
   
 #__________________________________________________________________
  if value_mg >= 3:
 
    if data[siete]['open'] < data[siete]['close']: 
      vela7 = 1 
    else:
      vela7 = -1  
   
 #_________________________________________________________________
  if value_mg >= 4:
   
    if data[ocho]['open'] < data[ocho]['close']: 
      vela8 = 1 
    else:
      vela8 = -1  
   

  if value_mg >= 5:
  
    if data[nueve]['open'] < data[nueve]['close']: 
      vela9 = 1 
    else:
      vela9 = -1  
   
   
  #____________________________________________________________________________
  
  
  mhi = vela0 + vela1 + vela2
  mg = vela4 
 
  if mhi > 0 and mg > 0:
    color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
    color_catalogo = "spring green" 
   else:      
    color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela4 != vela5:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela5 != vela6: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela6 != vela7:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela7 != vela8: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela8 != vela9: 
          color_catalogo = "spring green"
          puntos_mg="G5" 
  
  return color_catalogo, puntos_mg     
 except:
     print("error5")
  



def catalogo_cuadro5(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 3: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 3: numero_velas = 2 
    
    if numero_velas == 1:
     x = 7
    if numero_velas == 2:
     x = 2
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       
       color2, puntos2 = catalogo_mhi_velas5(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion5(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error5")    

def catalogo_mhi_velas6(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1
 
  if data[cinco]['open'] < data[cinco]['close']: 
    vela5 = 1 
  else:
    vela5 = -1  
      
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:

      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1 
       
 #______________________________________________________________________     
  if value_mg >= 2:
  
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1 
       
  
 #__________________________________________________________________
  if value_mg >= 3:

      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
   
 #_________________________________________________________________
  if value_mg >= 4:

      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  if value_mg >= 5:
    
      if data[diez]['open'] < data[diez]['close']: 
       vela10 = 1 
      else:
       vela10 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0 + vela1 + vela2
  mg = vela5 
 
  if mhi > 0 and mg > 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela5 != vela6:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela6 != vela7: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela7 != vela8:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela8 != vela9: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela9 != vela10: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
    print("error6")
  


def catalogo_cuadro6(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 2: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 2: numero_velas = 2 
    
    if numero_velas == 1:
     x = 7
    if numero_velas == 2:
     x = 2
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x
    diez2 = 5 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       diez2 = diez2 + 5
       
       color2, puntos2 = catalogo_mhi_velas6(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2,diez2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion6(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error6")   
  
def catalogo_mhi_velas7(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1
 
  if data[cinco]['open'] < data[cinco]['close']: 
    vela5 = 1 
  else:
    vela5 = -1  
      
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:

      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1 
       
 #______________________________________________________________________     
  if value_mg >= 2:
  
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1 
       
  
 #__________________________________________________________________
  if value_mg >= 3:

      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
   
 #_________________________________________________________________
  if value_mg >= 4:

      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  if value_mg >= 5:
    
      if data[diez]['open'] < data[diez]['close']: 
       vela10 = 1 
      else:
       vela10 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0 + vela1 + vela2 + vela3  + vela4
  mg = vela5 
 
  if mhi > 0 and mg < 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg > 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela5 != vela6:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela6 != vela7: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela7 != vela8:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela8 != vela9: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela9 != vela10: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
     print("error7")
  



def catalogo_cuadro7(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 4: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 4: numero_velas = 2  
    
    if numero_velas == 1:
     x = 5
    if numero_velas == 2:
     x = 0
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x
    diez2 = 5 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       diez2 = diez2 + 5
       
       
       
       color2, puntos2 = catalogo_mhi_velas7(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2,diez2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion7(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error7")      

def catalogo_mhi_velas8(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1
 
  if data[cinco]['open'] < data[cinco]['close']: 
    vela5 = 1 
  else:
    vela5 = -1  
      
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:

      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1 
       
 #______________________________________________________________________     
  if value_mg >= 2:
  
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1 
       
  
 #__________________________________________________________________
  if value_mg >= 3:

      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
   
 #_________________________________________________________________
  if value_mg >= 4:

      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  if value_mg >= 5:
    
      if data[diez]['open'] < data[diez]['close']: 
       vela10 = 1 
      else:
       vela10 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0 + vela1 + vela2 + vela3 + vela4
  mg = vela5 
 
  if mhi > 0 and mg > 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela5 != vela6:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela6 != vela7: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela7 != vela8:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela8 != vela9: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela9 != vela10: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
     print("error8")
  



def catalogo_cuadro8(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 4: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 4: numero_velas = 2  
    
    if numero_velas == 1:
     x = 5
    if numero_velas == 2:
     x = 0
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x
    diez2 = 5 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       diez2 = diez2 + 5
       
       
 
       color2, puntos2 = catalogo_mhi_velas8(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2,diez2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion8(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error8")    

def catalogo_mhi_velas9(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1
 
 
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:
      
      if data[cinco]['open'] < data[cinco]['close']: 
        vela5 = 1 
      else:
        vela5 = -1  
          
       
 #______________________________________________________________________     
  if value_mg >= 2:
      
      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1  
       
  
 #__________________________________________________________________
  if value_mg >= 3:
      
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1


 #_________________________________________________________________
  if value_mg >= 4:
      
      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
       
   
  if value_mg >= 5:
    
      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0
  mg = vela4 
 
  if mhi > 0 and mg > 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela4 != vela5:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela5 != vela6: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela6 != vela7:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela7 != vela8: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela8 != vela9: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
     print("error9")
  



def catalogo_cuadro9(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 0: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 5: numero_velas = 2 
    
    if numero_velas == 1:
     x = 10
    if numero_velas == 2:
     x = 5
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       
       color2, puntos2 = catalogo_mhi_velas9(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion9(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error9")
  
def catalogo_mhi_velas10(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
 
 
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:
      
     if data[dos]['open'] < data[dos]['close']: 
      vela2 = 1 
     else:
      vela2 = -1 
          
       
 #______________________________________________________________________     
  if value_mg >= 2:
      
      if data[tres]['open'] < data[tres]['close']: 
       vela3 = 1 
      else:
       vela3 = -1  
       
  
 #__________________________________________________________________
  if value_mg >= 3:
      
                 
      if data[cuatro]['open'] < data[cuatro]['close']: 
        vela4 = 1 
      else:
        vela4 = -1


 #_________________________________________________________________
  if value_mg >= 4:
      
      if data[cinco]['open'] < data[cinco]['close']: 
       vela5 = 1 
      else:
       vela5 = -1 
       
   
  if value_mg >= 5:
    
      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0
  mg = vela1
 
  if mhi > 0 and mg > 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela1 != vela2:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela2 != vela3: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela3 != vela4:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela4 != vela5: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela5 != vela6: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
     print("error10")
  



def catalogo_cuadro10(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 0: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 5: numero_velas = 2 
    
    if numero_velas == 1:
     x = 10
    if numero_velas == 2:
     x = 5
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       
       color2, puntos2 = catalogo_mhi_velas10(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion10(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error10")

def catalogo_mhi_velas11(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez,once): 
 try: 
  color_catalogo = ""
  puntos_mg = ""
  
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  
 
  if data[seis]['open'] < data[seis]['close']: 
    vela6 = 1 
  else:
    vela6 = -1  
      
      
 #__________________________Martin Gale_______________________________________
       
 #______________________________________________________________________     
  if value_mg >= 1:
  
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1 
       
  
 #__________________________________________________________________
  if value_mg >= 2:

      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
   
 #_________________________________________________________________
  if value_mg >= 3:

      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  if value_mg >= 4:
    
      if data[diez]['open'] < data[diez]['close']: 
       vela10 = 1 
      else:
       vela10 = -1 
       
  if value_mg >= 5:
    
      if data[once]['open'] < data[once]['close']: 
       vela11 = 1 
      else:
       vela11 = -1  
  #____________________________________________________________________________
  
  

  mhi = vela0 + vela1 + vela2
  mg = vela6
 
  if mhi > 0 and mg > 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg < 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela6 != vela7:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela7 != vela8: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela8 != vela9:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela9 != vela10: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela10 != vela11: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 except:
    print("error11")
  


def catalogo_cuadro11(martingala,divisa,new_data,min_actual):
  try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 2: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 2: numero_velas = 2 
    
    if numero_velas == 1:
     x = 6
    if numero_velas == 2:
     x = 1
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x
    diez2 = 5 + x
    once2 = 6 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       diez2 = diez2 + 5
       once2 = once2 + 5
       
       color2, puntos2 = catalogo_mhi_velas11(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2,diez2,once2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion11(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  except: print ("error11")

def catalogo_mhi_velas12(value_mg,data,cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve): 
 #try: 
  color_catalogo = ""
  puntos_mg = ""
 
  if data[cero]['open'] < data[cero]['close']: 
   vela0 = 1 
  else:
   vela0 = -1
  
  if data[uno]['open'] < data[uno]['close']: 
   vela1 = 1 
  else:
   vela1 = -1
       
  if data[dos]['open'] < data[dos]['close']: 
   vela2 = 1 
  else:
   vela2 = -1
   
  if data[tres]['open'] < data[tres]['close']: 
   vela3 = 1 
  else:
   vela3 = -1
    
  if data[cuatro]['open'] < data[cuatro]['close']: 
    vela4 = 1 
  else:
    vela4 = -1
 
 
      
 #__________________________Martin Gale_______________________________________
  
  if value_mg >= 1:
      
      if data[cinco]['open'] < data[cinco]['close']: 
        vela5 = 1 
      else:
        vela5 = -1  
          
       
 #______________________________________________________________________     
  if value_mg >= 2:
      
      if data[seis]['open'] < data[seis]['close']: 
       vela6 = 1 
      else:
       vela6 = -1  
       
  
 #__________________________________________________________________
  if value_mg >= 3:
      
      if data[siete]['open'] < data[siete]['close']: 
       vela7 = 1 
      else:
       vela7 = -1


 #_________________________________________________________________
  if value_mg >= 4:
      
      if data[ocho]['open'] < data[ocho]['close']: 
       vela8 = 1 
      else:
       vela8 = -1 
       
   
  if value_mg >= 5:
    
      if data[nueve]['open'] < data[nueve]['close']: 
       vela9 = 1 
      else:
       vela9 = -1 
       
   
  #____________________________________________________________________________
  
  

  mhi = vela0 + vela1 + vela2
  mg = vela4 
 
  if mhi > 0 and mg < 0:
     color_catalogo = "spring green" 
  else:
   if mhi < 0 and mg > 0:
     color_catalogo = "spring green" 
   else:      
     color_catalogo = "IndianRed1"    
#______________________________________________________________________________  
  if value_mg >= 1 and color_catalogo == "IndianRed1" and vela4 != vela5:
      color_catalogo = "spring green" 
      puntos_mg="G1"
  else: 
    if value_mg >= 2 and color_catalogo == "IndianRed1" and vela5 != vela6: 
       color_catalogo = "spring green"
       puntos_mg="G2"
    else: 
     if value_mg >= 3 and color_catalogo == "IndianRed1" and vela6 != vela7:
        color_catalogo = "spring green" 
        puntos_mg="G3"
     else:  
      if value_mg >= 4 and color_catalogo == "IndianRed1" and vela7 != vela8: 
         color_catalogo = "spring green" 
         puntos_mg="G4"
      else: 
       if value_mg >= 5 and color_catalogo == "IndianRed1" and vela8 != vela9: 
          color_catalogo = "spring green"
          puntos_mg="G5"         
  
  return color_catalogo, puntos_mg     
 #except:
   #  print("error12")
  



def catalogo_cuadro12(martingala,divisa,new_data,min_actual):
  #try:
    color = []
    puntos = []
    porciento_green = 0
    
    if martingala == "MG0": mg_cantidad = 0 
    if martingala == "MG1": mg_cantidad = 1 
    if martingala == "MG2": mg_cantidad = 2
    if martingala == "MG3": mg_cantidad = 3
    if martingala == "MG4": mg_cantidad = 4
    if martingala == "MG5": mg_cantidad = 5 
    
    if min_actual == 0 and mg_cantidad <= 0: numero_velas = 1 
    if min_actual == 5 and mg_cantidad <= 0: numero_velas = 1
    if min_actual == 0 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 5 and mg_cantidad >= 1: numero_velas = 2
    if min_actual == 1 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 6 and mg_cantidad <= 1: numero_velas = 1
    if min_actual == 1 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 6 and mg_cantidad >= 2: numero_velas = 2
    if min_actual == 2 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 7 and mg_cantidad <= 2: numero_velas = 1
    if min_actual == 2 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 7 and mg_cantidad >= 3: numero_velas = 2
    if min_actual == 3 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 8 and mg_cantidad <= 3: numero_velas = 1
    if min_actual == 3 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 8 and mg_cantidad >= 4: numero_velas = 2
    if min_actual == 4 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 9 and mg_cantidad <= 4: numero_velas = 1
    if min_actual == 4 and mg_cantidad >= 5: numero_velas = 2
    if min_actual == 9 and mg_cantidad >= 5: numero_velas = 2 
    
    if numero_velas == 1:
     x = 10
    if numero_velas == 2:
     x = 5
    
    porciento_final = 0
    porciento_green = 0
     
    cero2 = -5 + x
    uno2 = -4 + x
    dos2 = -3 + x
    tres2 = -2 + x
    cuatro2 = -1 + x
    cinco2 = 0 + x
    seis2 = 1 + x
    siete2 = 2 + x
    ocho2 = 3 + x
    nueve2 = 4 + x

    n = 0
    while n < 40:
       n = n + 1 
       cero2 = cero2 + 5
       uno2 = uno2 + 5
       dos2 = dos2 + 5
       tres2 = tres2 + 5  
       cuatro2 = cuatro2 + 5
       cinco2 = cinco2 + 5
       seis2 = seis2 + 5 
       siete2 = siete2 + 5
       ocho2 = ocho2 + 5
       nueve2 = nueve2 + 5
       
       color2, puntos2 = catalogo_mhi_velas12(mg_cantidad,new_data,cero2,uno2,dos2,tres2,cuatro2,cinco2,seis2,siete2,ocho2,nueve2)
       color.append(color2)
       puntos.append(puntos2)
       
       if color2 == "spring green": porciento_green = porciento_green + 1

    porciento_final = (porciento_green/ 40)*100   
    if porciento_final >= 90: fg_porciento = "spring green" 
    if porciento_final >= 80 and porciento_final <90: fg_porciento = "DarkOrange1"
    if porciento_final >= 0 and porciento_final <80: fg_porciento = "IndianRed2"
    operacion12(color,puntos,porciento_final,fg_porciento,divisa,mg_cantidad)
  #except: print ("error12") 
  
def llamar_velas(_martingala,divisa):
  
  cata_go = threading.Thread(target=catalogo_start, args=(_martingala,divisa))
  cata_go.start()
    
def catalogo_start(_martingala,divisa):
   if divisa != "USDZAR-OTC" and divisa != "USDINR-OTC" and divisa != "USDHKD-OTC" and divisa != "USDSGD-OTC" and divisa != "USDZAR" and divisa != "USDINR" and divisa != "USDHKD" and divisa != "USDSGD": 
    global divisa_default
    divisa_default = divisa
    numero_velas = 0
    now = datetime.now()
    min_catalogo = format(now.minute)
    seg_catalogo = format(now.second)
    _min_catalogo = int(min_catalogo)
    cantidad_de_velas = _min_catalogo % 10;
   
    if cantidad_de_velas == 0: numero_velas = 11 + 200
    if cantidad_de_velas == 5: numero_velas = 11 + 200
   
    if cantidad_de_velas == 1: numero_velas = 12 + 200
    if cantidad_de_velas == 6: numero_velas = 12 + 200
    
    if cantidad_de_velas == 2: numero_velas = 13 + 200
    if cantidad_de_velas == 7: numero_velas = 13 + 200
    
    if cantidad_de_velas == 3: numero_velas = 14 + 200
    if cantidad_de_velas == 8: numero_velas = 14 + 200
    
    if cantidad_de_velas == 4: numero_velas = 15 + 200
    if cantidad_de_velas == 9: numero_velas = 15 + 200
    
    
    if seg_catalogo == "0" or seg_catalogo ==  "1":
        time.sleep(3)
    
    data_all = api.get_candles(divisa, 60, numero_velas, time.time())
    contador = len(data_all)

    h1 = threading.Thread(target=catalogo_cuadro1, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h1.start()
    
    h2 = threading.Thread(target=catalogo_cuadro2, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h2.start() 
    
    h3 = threading.Thread(target=catalogo_cuadro3, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h3.start()
    
    h4 = threading.Thread(target=catalogo_cuadro4, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h4.start()
    
    h5 = threading.Thread(target=catalogo_cuadro5, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h5.start()
    
    h6 = threading.Thread(target=catalogo_cuadro6, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h6.start()
    
    h7 = threading.Thread(target=catalogo_cuadro7, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h7.start()
    
    h8 = threading.Thread(target=catalogo_cuadro8, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h8.start()
    
    h9 = threading.Thread(target=catalogo_cuadro9, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h9.start()
    
    h10 = threading.Thread(target=catalogo_cuadro10, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h10.start()
    
    h11 = threading.Thread(target=catalogo_cuadro11, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h11.start()
    
    h12 = threading.Thread(target=catalogo_cuadro12, args=(_martingala,divisa,data_all,cantidad_de_velas))  
    h12.start()
    
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    h5.join()
    h6.join()
    h7.join()
    h8.join()
    h9.join()
    h10.join()
    h11.join()
    h12.join()
    
    ht = threading.Thread(target=estadisticas_totales, args=(_martingala,))  
    ht.start()
    
imagen_inicio=PhotoImage(file="inicio.gif")    
lbl_inicio=Label(image=imagen_inicio)
lbl_inicio.place(x=0, y=0)

   
btn_inicio_entrar = Button(borderwidth = 0, image=inicio_entrar_foto, bg = color_fondo, command = lambda:[app.after(200,guardar_credenciales2)])
btn_inicio_entrar.place(x=498, y=412)

correo_inicio = Entry(width=42, textvariable= "e-mail")
correo_inicio.place(x=550, y=276)

contra_inicio = Entry(width=42, textvariable= "password")
contra_inicio.place(x=550, y=333)

check_credenciales2_var = IntVar()
check_credenciales2_var.set(1)
check_credenciales2 = Checkbutton(bg = color_fondo,activebackground = color_fondo,variable = check_credenciales2_var)
check_credenciales2.place(x=505, y=376)

def delete_inicio():
   lbl_inicio.destroy()
   btn_inicio_entrar.destroy()
   correo_inicio.destroy()
   contra_inicio.destroy()
   check_credenciales2.destroy()
   
def guardar_credenciales2():
   if check_credenciales2_var.get() == 1: 
    file2 = open("config/Readme2.txt", "w") 
    file2.write(correo_inicio.get()+"\n")
    file2.write(contra_inicio.get())
    file2.close()
   else: 
    file2 = open("config/Readme2.txt", "w") 
    file2.write(""+"\n")
    file2.write("")
    file2.close()
   delete_inicio()

file2 = open("config/Readme2.txt", "r")
credenciales2_get = file2.readlines()
file2.close()
count_credenciales2 = len(credenciales2_get)
if count_credenciales2 >= 1:
  correo_default2=credenciales2_get[0][:-1]   
  correo_inicio.insert(0,correo_default2) 
if count_credenciales2 >= 2:
  contra_inicio.insert(0,credenciales2_get[1]) 

  
   
app.mainloop()     
     
    
    
          