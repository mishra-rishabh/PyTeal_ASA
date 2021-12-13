from pyteal import *

def freezeAsset( assetId: TealType.uint64 , freezeAddress: TealType.bytes ):
  isFreezed = Int( 1 )

  return Seq( [
    InnerTxnBuilder.Begin() ,
    InnerTxnBuilder.SetFields( {
      TxnField.type_enum: TxnType.AssetFreeze ,
      TxnField.freeze_asset: assetId ,
      TxnField.freeze_asset_frozen: isFreezed ,
      TxnField.freeze_asset_account: freezeAddress
    } ) ,

    InnerTxnBuilder.Submit() ,
    Int( 1 )
  ] )

if __name__ == "__main__":
  with open( "tealFiles/freezeASA.teal" , "w" ) as f:
    program = compileTeal( freezeAsset( Int( 1 ) , Bytes( "ZBLZXNUGJJRWWGI5GJY5DG4ERALP2BECPXSCAO7AXQTHL2Q5ALQNTPCKPU" ) ) ,  Mode.Application , version = 5 )
    f.write( program )