Summary:	Bing, a point-to-point bandwidth measurement tool (b from Bandwitch)
Summary(pl):	Bing, narzêdzie s³u¿±ce mierzeniu przepustowo¶ci ³±czy 
Name:		bing
Version:	1.0.4
Release:	2
License:	BSD
Group:		Net/Utilities
Group(pl):	Sieæ/Narzêdzia
Source0:	http://www.fibrespeed.net/~mbabcock/mirrors/bing/%{name}-%{version}.tar.bz2
Patch0:		%{name}.patch
URL:		http://web.cnam.fr/reseau/bing.html

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bing determines the real (raw, as opposed to available or average)
throughput on a link by measuring ICMP echo requests roundtrip times
for different packet sizes for each end of the link.

%description -l pl
Bing oblicza aktualn± (w przeciwieñstwie do np. ¶redniej)
przepustowow¶æ ³±cza mierz±c czasy powrotu odpowiedzi na komunikaty
ICMP.

%prep 
rm -rf %{RPM_BUILD_ROOT}
%setup -q
%patch -p0 

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d %{RPM_BUILD_ROOT}%{_bindir}/
install bing %{RPM_BUILD_ROOT}%{_bindir}/bing
gzip -9nf README bing.ps ChangeLog
install bing.8 %{_mandir}/man8

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bing
%doc {README,ChangeLog,bing.ps}.gz 
%{_mandir}/man8/bing.8
