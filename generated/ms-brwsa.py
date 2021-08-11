"""
Generated from MIDL2Impacket.py
"""


from __future__ import division
from __future__ import print_function
from impacket.dcerpc.v5.ndr import *
from impacket.dcerpc.v5.dtypes import *
from impacket.dcerpc.v5.lsad import PRPC_UNICODE_STRING_ARRAY
from impacket.structure import Structure
from impacket import nt_errors
from impacket.uuid import uuidtup_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException

DWORD64 = NDRUHYPER
__INT64 = NDRHYPER
class CONTEXT_HANDLE(NDRSTRUCT):
    align = 1
    structure = (
        ('Data', '20s=""'),
    )
HANDLE_T = CONTEXT_HANDLE
class RPC_STRING(NDRSTRUCT):
    structure = (
        ('Length','<H=0'),
        ('MaximumLength','<H=0'),
        ('Data',LPSTR),
    )

    def __setitem__(self, key, value):
        if key == 'Data' and isinstance(value, NDR) is False:
            self['Length'] = len(value)
            self['MaximumLength'] = len(value)
        return NDRSTRUCT.__setitem__(self, key, value)

    def dump(self, msg = None, indent = 0):
        if msg is None: msg = self.__class__.__name__
        if msg != '':
            print("%s" % msg, end=' ')

        if isinstance(self.fields['Data'] , NDRPOINTERNULL):
            print(" NULL", end=' ')
        elif self.fields['Data']['ReferentID'] == 0:
            print(" NULL", end=' ')
        else:
            return self.fields['Data'].dump('',indent)

class PRPC_STRING(NDRPOINTER):
    referent = (
        ('Data', RPC_STRING),
    )

UNSIGNED_SHORT = NDRUSHORT
UNSIGNED_CHAR = NDRCHAR
UNSIGNED_LONG = NDRULONG
UNSIGNED_INT = NDRULONG
UNSIGNED___INT64 = NDRUHYPER
SIGNED___INT64 = NDRHYPER
SIGNED_INT = NDRSHORT
SIGNED_LONG = NDRLONG
SIGNED_CHAR = NDRCHAR
SIGNED_SHORT = NDRSHORT
CONST_WCHAR_T = WSTR
CONST_CHAR = NDRCHAR
CONST_INT = NDRLONG
CONST_VOID = CONTEXT_HANDLE
CONST_LONG = NDRLONG
VOID = CONTEXT_HANDLE
__INT3264 = NDRLONG
UNSIGNED___INT3264 = NDRULONG
CONST_UNSIGNED_LONG = NDRULONG
UNSIGNED_HYPER = NDRUHYPER
HYPER = NDRHYPER

#################################################################################

#TYPEDEFS

#################################################################################

#################################################################################

#INTERFACE DEFINITION

#################################################################################

#################################################################################

#browser Definition

#################################################################################

MSRPC_UUID_BROWSER = uuidtup_to_bin(('6BFFD098-A112-3610-9833-012892020162','0.0'))

LPWSTR = WCHAR
BROWSER_IDENTIFY_HANDLE = LPWSTR

class SERVER_INFO_100_CONTAINER(NDRSTRUCT):
    structure = (
        ('EntriesRead', DWORD),('Buffer', LPSERVER_INFO_100),
    )
class PSERVER_INFO_100_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100_CONTAINER),
    )    
class LPSERVER_INFO_100_CONTAINER(NDRPOINTER):
    referent = (
        ('Data', SERVER_INFO_100_CONTAINER),
    )    


class SERVERINFO(NDRUNION):
    union = {
        100: ('Level100',LPSERVER_INFO_100_CONTAINER),
    }
        

class SERVER_ENUM_STRUCT(NDRSTRUCT):
    structure = (
        ('Level', DWORD),('ServerInfo', SERVERINFO),
    )
class PSERVER_ENUM_STRUCT(NDRPOINTER):
    referent = (
        ('Data', SERVER_ENUM_STRUCT),
    )    
class LPSERVER_ENUM_STRUCT(NDRPOINTER):
    referent = (
        ('Data', SERVER_ENUM_STRUCT),
    )    


class Opnum0NotUsedOnWire(NDRCALL):
    opnum = 0
    structure = (

    )

class Opnum0NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum1NotUsedOnWire(NDRCALL):
    opnum = 1
    structure = (

    )

class Opnum1NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class I_BrowserrQueryOtherDomains(NDRCALL):
    opnum = 2
    structure = (
		('ServerName', BROWSER_IDENTIFY_HANDLE),
		('InfoStruct', LPSERVER_ENUM_STRUCT),
    )

class I_BrowserrQueryOtherDomainsResponse(NDRCALL):
    structure = (
		('InfoStruct', LPSERVER_ENUM_STRUCT),
		('TotalEntries', LPDWORD),
    )
        

class Opnum3NotUsedOnWire(NDRCALL):
    opnum = 3
    structure = (

    )

class Opnum3NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum4NotUsedOnWire(NDRCALL):
    opnum = 4
    structure = (

    )

class Opnum4NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum5NotUsedOnWire(NDRCALL):
    opnum = 5
    structure = (

    )

class Opnum5NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum6NotUsedOnWire(NDRCALL):
    opnum = 6
    structure = (

    )

class Opnum6NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum7NotUsedOnWire(NDRCALL):
    opnum = 7
    structure = (

    )

class Opnum7NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum8NotUsedOnWire(NDRCALL):
    opnum = 8
    structure = (

    )

class Opnum8NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum9NotUsedOnWire(NDRCALL):
    opnum = 9
    structure = (

    )

class Opnum9NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum10NotUsedOnWire(NDRCALL):
    opnum = 10
    structure = (

    )

class Opnum10NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        

class Opnum11NotUsedOnWire(NDRCALL):
    opnum = 11
    structure = (

    )

class Opnum11NotUsedOnWireResponse(NDRCALL):
    structure = (

    )
        
OPNUMS = {
0 : (Opnum0NotUsedOnWire,Opnum0NotUsedOnWireResponse),
1 : (Opnum1NotUsedOnWire,Opnum1NotUsedOnWireResponse),
2 : (I_BrowserrQueryOtherDomains,I_BrowserrQueryOtherDomainsResponse),
3 : (Opnum3NotUsedOnWire,Opnum3NotUsedOnWireResponse),
4 : (Opnum4NotUsedOnWire,Opnum4NotUsedOnWireResponse),
5 : (Opnum5NotUsedOnWire,Opnum5NotUsedOnWireResponse),
6 : (Opnum6NotUsedOnWire,Opnum6NotUsedOnWireResponse),
7 : (Opnum7NotUsedOnWire,Opnum7NotUsedOnWireResponse),
8 : (Opnum8NotUsedOnWire,Opnum8NotUsedOnWireResponse),
9 : (Opnum9NotUsedOnWire,Opnum9NotUsedOnWireResponse),
10 : (Opnum10NotUsedOnWire,Opnum10NotUsedOnWireResponse),
11 : (Opnum11NotUsedOnWire,Opnum11NotUsedOnWireResponse),
}

