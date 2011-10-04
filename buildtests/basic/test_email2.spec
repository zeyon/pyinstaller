# -*- mode: python -*-

__testname__ = 'test_email2'

a = Analysis([os.path.join(HOMEPATH,'support/_mountzlib.py'),
              os.path.join(CONFIGDIR,'support/useUnicode.py'),
              __testname__ + '.py'],
             pathex=[])

for m in a.pure:
    if m[0] == 'email.mime.multipart':
        break
else:
    raise SystemExit('hook for email.MIMEMultipart failed')

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.linux2/test-email2', __testname__ + '.exe'),
          debug=False,
          strip=False,
          upx=False,
          console=1 )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name=os.path.join('dist', __testname__))