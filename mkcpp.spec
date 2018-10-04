Name:           mkcpp
Version:        1.0.0
Release:        1%{?dist}
Summary:        Create a empty c++ file with main declared

License:        LGPLv3+
URL:            https://github.com/astrobit/mkcpp
Source0:        https://www.astronaos.com/mkcpp/mkcpp-1.0.0.tar.gz


BuildRequires:  gcc
#Requires:       

%description
This is a relatively simple script that creates a c++ file that is empty other
than a main function.

%prep
%autosetup


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{_bindir}/*

%changelog
* Thu Oct 4 2018 Brian W. Mulligan <bwmulligan@astronaos.com>
- Initial RPM release


