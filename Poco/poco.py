
#---------------------------------------------Tile-------------------------------------------------------#
__author__ = "QC"
__title__ ="List Poco"
__desc__="""
    Tong hop danh sach cac poco in game
"""
#---------------------------------------------End Tile---------------------------------------------------#
#---------------------------------------------Import LIB-------------------------------------------------#
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
#---------------------------------------------End Import Lib---------------------------------------------#
#---------------------------------------------Link-------------------------------------------------------#
from Lavuavi.Poco.poco import *
#---------------------------------------------Link-------------------------------------------------------#
#---------------------------------------------Import FILE------------------------------------------------#

#---------------------------------------------End Import FILE--------------------------------------------#

#---------------------------------------------Connect Device---------------------------------------------#
if not cli_setup():
    auto_setup(__file__)
#------------------------------------------End Connect---------------------------------------------------#

#------------------------------------------Poco----------------------------------------------------------#
poco = CocosJsPoco() 
#------------------------------------------End Poco------------------------------------------------------#
#------------------------------------------script content------------------------------------------------#
#------------------------------------------bien----------------------------------------------#
x=0
#------------------------------------------end bien------------------------------------------#
#------------------------------------------WC------------------------------------------------#

#------------------------------------------WC------------------------------------------------#
#------------------------------------------VIP-----------------------------------------------#

#------------------------------------------VIP-----------------------------------------------#
#------------------------------------------DB------------------------------------------------#

#------------------------------------------DB------------------------------------------------#
#---------------------------------------------End script--------------------------------------------------------------------#
#---------------------------------------------Report-----------------------------------------------------#
#File report
#---------------------------------------------End Report-------------------------------------------------#