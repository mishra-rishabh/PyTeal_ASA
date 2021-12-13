from pyteal import *

def create_asa( txnIndex: TealType.uint64 ):
  asset_name = Bytes( "PENGUIN" )
  unit_name = Bytes( "penguin" )
  total_amount = Int( 2000 )
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

if __name__ == "__main__":
  with open( "tealFiles/createasa.teal" , "w" ) as f:
    program = compileTeal( create_asa( Int( 1 ) ) ,  Mode.Application , version = 5 )
    f.write( program )

# program = compileTeal( create_asa() ,  Mode.Application , version=5 )
# print( program )
