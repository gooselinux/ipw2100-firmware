Summary: Firmware for Intel® PRO/Wireless 2100 network adaptors
Name: ipw2100-firmware
Version: 1.3
Release: 11%{?dist}
License: Redistributable, no modification permitted
Group: System Environment/Kernel
URL: http://ipw2100.sourceforge.net/firmware.php
# License agreement must be displayed before download (referer protection)
Source: ipw2100-fw-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
# This is so that the noarch packages only appears for these archs
ExclusiveArch: noarch i386 x86_64

%description
This package contains the firmware files required by the ipw2100 driver for
Linux. Usage of the firmware is subject to the terms and conditions contained
in /lib/firmware/LICENSE.ipw2100. Please read it carefully.


%prep
%setup -q -c


%build


%install
%{__rm} -rf %{buildroot} _doc/
%{__mkdir_p} %{buildroot}/lib/firmware
# Terms state that the LICENSE *must* be in the same directory as the firmware
%{__install} -p -m 0644 *.fw %{buildroot}/lib/firmware/
%{__install} -p -m 0644 LICENSE %{buildroot}/lib/firmware/LICENSE.ipw2100
# Symlink to include as %%doc
%{__mkdir} _doc
%{__ln_s} /lib/firmware/LICENSE.ipw2100 _doc/LICENSE


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc _doc/*
/lib/firmware/LICENSE.ipw2100
/lib/firmware/*.fw


%changelog
* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 1.3-11
- Add dist tag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar 20 2007 Matthias Saou <http://freshrpms.net> 1.3-8
- Add "noarch" to the ExclusiveArchs since plague chokes otherwise.

* Mon Mar  5 2007 Matthias Saou <http://freshrpms.net> 1.3-7
- Change group and license fields to reflect latest firmware guidelines.

* Sat Feb 24 2007 Matthias Saou <http://freshrpms.net> 1.3-6
- Fix group and license tags.
- Add (partially useful) exclusivearch.
- Quiet %%setup.

* Wed Feb 14 2007 Matthias Saou <http://freshrpms.net> 1.3-5
- Don't mark the LICENSE in /lib/firmware as %%doc since it could be excluded
  when using --excludedocs, symlink a file in %%doc to it instead.

* Wed Feb 14 2007 Matthias Saou <http://freshrpms.net> 1.3-4
- Minor spec file cleanup for Fedora inclusion.

* Tue Oct 17 2006 Matthias Saou <http://freshrpms.net> 1.3-3
- Move the LICENSE as LICENSE.ipw2100 in the firmware directory to fully
  comply to the Intel redistribution terms and conditions.

* Mon Jan  2 2006 Matthias Saou <http://freshrpms.net> 1.3-2
- Convert spec file to UTF-8.
- Remove all symlinks to keep only /lib/firmware like in ipw2200-firmware.

* Wed Nov  3 2004 Matthias Saou <http://freshrpms.net> 1.3-1
- Now put the files in /lib/firmware and symlinks in other dirs.

* Tue Sep 28 2004 Matthias Saou <http://freshrpms.net> 1.3-1
- Update to 1.3.

* Wed Aug 25 2004 Matthias Saou <http://freshrpms.net> 1.2-1
- Update to 1.2.

* Wed Jun 16 2004 Matthias Saou <http://freshrpms.net> 1.1-1
- Cosmetic spec file changes.

* Tue May 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to firmware version 1.1.

* Tue May 11 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Change description to explicitly point to the LICENSE file.

* Sat May  8 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

