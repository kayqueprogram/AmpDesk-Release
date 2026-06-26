# Set required environment variables using API to avoid PS parsing bugs
[System.Environment]::SetEnvironmentVariable('INCLUDE', 'C:\Program Files (x86)\Windows Kits\10\Include\10.0.26100.0\ucrt;C:\Program Files (x86)\Windows Kits\10\Include\10.0.26100.0\shared;C:\Program Files (x86)\Windows Kits\10\Include\10.0.26100.0\um;C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\include')
[System.Environment]::SetEnvironmentVariable('LIB', 'C:\Program Files (x86)\Windows Kits\10\Lib\10.0.26100.0\ucrt\x64;C:\Program Files (x86)\Windows Kits\10\Lib\10.0.26100.0\um\x64;C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\lib\x64')
[System.Environment]::SetEnvironmentVariable('PATH', 'C:\Program Files\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64;C:\Program Files\LLVM\bin;' + $env:PATH)
[System.Environment]::SetEnvironmentVariable('LIBCLANG_PATH', 'C:\Program Files\LLVM\bin')
[System.Environment]::SetEnvironmentVariable('BINDGEN_EXTRA_CLANG_ARGS', '--target=x86_64-pc-windows-msvc')
[System.Environment]::SetEnvironmentVariable('VCPKG_ROOT', 'C:\vcpkg')
[System.Environment]::SetEnvironmentVariable('VCPKG_INSTALLED_ROOT', 'C:\vcpkg\installed')

# Build the installer using python build.py
python build.py --flutter --hwcodec
