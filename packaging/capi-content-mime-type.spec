Name:       capi-content-mime-type
Summary:    A MIME type library in Tizen C API
Version:    0.0.2
Release:    2
Group:      APIs
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Source1001: 	capi-content-mime-type.manifest
BuildRequires:  cmake
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(capi-base-common)
BuildRequires:  pkgconfig(xdgmime)

%description


%package devel
Summary:  A MIME type library in Tizen C API (Development)
Group:    APIs
Requires: %{name} = %{version}-%{release}
Requires:  pkgconfig(capi-base-common)

%description devel


%prep
%setup -q
cp %{SOURCE1001} .


%build
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`  
%cmake .  -DFULLVER=%{version} -DMAJORVER=${MAJORVER} 


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest %{name}.manifest
%{_libdir}/lib*.so.*
%manifest capi-content-mime-type.manifest

%files devel
%manifest %{name}.manifest
%{_includedir}/content/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so


