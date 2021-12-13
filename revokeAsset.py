from pyteal import *

def assetRevoke(
  assetID: TealType.uint64 , assetAmt: TealType.uint64 ,
  clawbackAddr: TealType.bytes , receiver: TealType.bytes
):
  return Seq( [
    InnerTxnBuilder.Begin() ,
    InnerTxnBuilder.SetFields( {
      TxnField.type_enum: TxnType.AssetTransfer ,
      TxnField.xfer_asset: assetID ,
      TxnField.asset_amount: assetAmt ,
      TxnField.asset_sender: clawbackAddr ,
      TxnField.asset_receiver: receiver
    } ) ,

    InnerTxnBuilder.Submit() ,
    Int( 1 )
  ] )

if __name__ == "__main__":
  with open( "tealFiles/revokeAsset.teal" , "w" ) as f:
    program = compileTeal( assetRevoke( Int( 1 ) , Int( 200 ) , Bytes( "ZNZKSKALDIEJSJAKA" ) , Bytes( "ZNZKSKALQOOPAKLL" ) ) , Mode.Application , version = 5 )
    f.write( program )