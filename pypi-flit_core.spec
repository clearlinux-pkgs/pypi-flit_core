#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-flit_core
Version  : 3.8.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/10/e5/be08751d07b30889af130cec20955c987a74380a10058e6e8856e4010afc/flit_core-3.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/10/e5/be08751d07b30889af130cec20955c987a74380a10058e6e8856e4010afc/flit_core-3.8.0.tar.gz
Summary  : Distribution-building parts of Flit. See flit package for more information
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-flit_core-license = %{version}-%{release}
Requires: pypi-flit_core-python = %{version}-%{release}
Requires: pypi-flit_core-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
flit_core bundles the 'tomli' TOML parser, to avoid a bootstrapping problem.
tomli is packaged using Flit, so there would be a dependency cycle when building
from source. Vendoring a copy of tomli avoids this. The code in tomli is under
the MIT license, and the LICENSE file is in the .dist-info folder.

%package license
Summary: license components for the pypi-flit_core package.
Group: Default

%description license
license components for the pypi-flit_core package.


%package python
Summary: python components for the pypi-flit_core package.
Group: Default
Requires: pypi-flit_core-python3 = %{version}-%{release}

%description python
python components for the pypi-flit_core package.


%package python3
Summary: python3 components for the pypi-flit_core package.
Group: Default
Requires: python3-core
Provides: pypi(flit_core)

%description python3
python3 components for the pypi-flit_core package.


%prep
%setup -q -n flit_core-3.8.0
cd %{_builddir}/flit_core-3.8.0
pushd ..
cp -a flit_core-3.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667842817
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flit_core
cp %{_builddir}/flit_core-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-flit_core/12276565e762cd50328b99b71e0343d3d99350a0 || :
cp %{_builddir}/flit_core-%{version}/flit_core/vendor/tomli-1.2.3.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-flit_core/9da6ca26337a886fb3e8d30efd4aeda623dc9ade || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flit_core/12276565e762cd50328b99b71e0343d3d99350a0
/usr/share/package-licenses/pypi-flit_core/9da6ca26337a886fb3e8d30efd4aeda623dc9ade

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
