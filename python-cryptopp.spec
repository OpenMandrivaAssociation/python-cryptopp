%define modname pycryptopp

Name:           python-cryptopp
Version:        0.5.29
Release:        1
Summary:        Python Wrappers for the Crypto++ Library
Url:            http://allmydata.org/trac/pycryptopp
License:        GPLv2+
Group:          Development/Python
Source:         http://pypi.python.org/packages/source/p/pycryptopp/%{modname}-%{version}.tar.gz
%{py_requires}
BuildRequires:  libcryptopp-devel python-setuptools #python-xml
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
  %{buildroot}%{python_sitearch}/%{modname}/test \
  %{buildroot}%{python_sitearch}/%{modname}/testvectors

%check
python setup.py test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING.GPL COPYING.TGPPL.html ChangeLog NEWS.rst README.txt
%{python_sitearch}/%{modname}
%{python_sitearch}/%{modname}-%{version}-*.egg-info
