%define modname pycryptopp

Name:           python-cryptopp
Version:        0.6.0.1206569328141510525648634803928199668821045408958
Release:        1
Summary:        Python Wrappers for the Crypto++ Library

Url:            http://allmydata.org/trac/pycryptopp
License:        GPLv2+
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
%{py_requires}
BuildRequires:  pkgconfig(cryptopp)
BuildRequires:  python-setuptools
BuildRequires:  python-pyxml
Patch0:         pycryptopp-0.5.29-disable-w-flag.patch

%description
pycryptopp is a set of Python wrappers for a few of the best crypto algorithms
from the  Crypto++ library. 

RSA-PSS-SHA256 signatures, ECDSA(1363)/EMSA1(SHA-256) signatures, SHA-256
hashes, and AES-CTR encryption for Python.

%prep
%setup -q -n %{modname}-%{version}
%patch0

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
python setup.py build --disable-embedded-cryptopp

%install
python setup.py install --single-version-externally-managed --prefix=%{_prefix} --root=%{buildroot}
rm -r \
  %{buildroot}%{_prefix}/embeddedcryptopp \
  %{buildroot}%{_datadir}/doc/%{modname} \
  %{buildroot}%{py_platsitedir}/%{modname}/test \
  %{buildroot}%{py_platsitedir}/%{modname}/testvectors

%check
python setup.py test

%files
%doc COPYING.GPL COPYING.TGPPL.html ChangeLog NEWS.rst README.txt
%{py_platsitedir}/%{modname}
%{py_platsitedir}/%{modname}-%{version}-*.egg-info



