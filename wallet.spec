# -*- mode: python -*-

block_cipher = None


a = Analysis(['wallet.py'],
             pathex=['C:\\code\\py\\this'],
             binaries=[('coin.ico', '.'), ('./Resources/bin/myntd.exe', '.'), ('./Resources/bin/myntnote-wallet-rpc.exe', '.'), ('./Resources/bin/mynt-wallet-cli.exe', '.'), ('./Resources/bin/libwinpthread-1.dll', '.'), ('./Resources/bin/libstdc++-6.dll', '.'), ('./Resources/bin/libgcc_s_seh-1.dll', '.'), ('./Resources/bin/libssl.a', '.'), ('./Resources/bin/libcrypto.a', '.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='wallet',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='coin.ico')
