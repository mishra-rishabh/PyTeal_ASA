from pyteal import *

def create_asa( txnIndex: TealType.uint64 ):
  asset_name = Bytes( "ARTEMIS" )
  unit_name = Bytes( "artemis" )
  total_amount = Int( 1000 )
  url = Bytes( "#" )
  decimals = Int( 0 )
  metadata_hash = Bytes( "#" )

  return Seq( [
    InnerTxnBuilder.Begin(),

    InnerTxnBuilder.SetFields( {
    TxnField.type_enum: TxnType.AssetConfig,
    TxnField.config_asset_clawback: Global.current_application_address(),
    TxnField.config_asset_reserve: Global.current_application_address(),
    TxnField.config_asset_default_frozen: Int(1),
    TxnField.config_asset_name: asset_name,
    TxnField.config_asset_unit_name: unit_name,
    TxnField.config_asset_total: total_amount,
    TxnField.config_asset_url: url,
    TxnField.config_asset_decimals: decimals,
    TxnField.config_asset_metadata_hash: metadata_hash,
    } ),

    InnerTxnBuilder.Submit(),
    InnerTxn.created_asset_id()
  ] )

assetID = create_asa( Int( 1 ) )
amount = Int( 3000 )
receiver = Bytes( "ZBLZXNUGJJRWWGI5GJY5DG4ERALP2BECPXSCAO7AXQTHL2Q5ALQNTPCKPU" )

def transfer_asa( assetID: TealType.uint64 , assetAmt: TealType.uint64 , receiver: TealType.bytes ):
  return Seq( [
    InnerTxnBuilder.Begin() ,

    InnerTxnBuilder.SetFields( {
      TxnField.type_enum: TxnType.AssetTransfer ,
      TxnField.xfer_asset: assetID ,
      TxnField.asset_amount: assetAmt ,
      TxnField.asset_receiver: receiver
    } ) ,

    InnerTxnBuilder.Submit() ,
    Int( 1 )
  ] )

if __name__ == "__main__":
  with open( "tealFiles/transferAsset.teal" , "w" ) as f:
    program = compileTeal( transfer_asa( assetID , amount , receiver ) , Mode.Application , version = 5 )
    f.write( program )