from pyteal import *

def destroyAsset( assetID: TealType.uint64 ):
  return Seq( [
    InnerTxnBuilder.Begin() ,

    InnerTxnBuilder.SetFields( {
      TxnField.type_enum: TxnType.AssetConfig ,
      TxnField.config_asset: assetID
    } ) ,

    InnerTxnBuilder.Submit() ,
    Int( 1 )
  ] )

if __name__ == "__main__":
  with open( "tealFiles/destroyAsset.teal" , "w" ) as f:
    program = compileTeal( destroyAsset( Int( 1 ) ) ,  Mode.Application , version = 5 )
    f.write( program )