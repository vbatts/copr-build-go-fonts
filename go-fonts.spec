%global git_commit		426cfd8eeb6e08ab1932954e09e3c2cb2bc6e36d
%global git_shortcommit		%(c=%{git_commit}; echo ${c:0:7})

# they warn against doing this ... :-\
%define _disable_source_fetch 0

Name:           go-fonts
Version:        0.1
Release:        0.git%{git_shortcommit}%{?dist}
Summary:        golang fonts

License:        ASL 2.0
URL:            https://blog.golang.org/go-fonts
Source0:        https://go.googlesource.com/image/+archive/%{git_commit}/font/gofont/ttfs.tar.gz
Source1:        %{name}.metainfo.xml
Source2:        30-0-go-fonts-fontconfig.conf
Source3:        62-go-fonts-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
Produced specifically for the Go Project by Bigelow and Holmes type foundry.

%prep
%setup -q -c -n ttfs


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/30-0-%{name}-fontconfig.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/62-%{name}-fontconfig.conf

ln -s %{_fontconfig_templatedir}/30-0-%{name}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/30-0-%{name}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/62-%{name}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/62-%{name}-fontconfig.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%_font_pkg -f *-%{name}-fontconfig.conf *.ttf
%doc
%{_datadir}/appdata/%{name}.metainfo.xml
%license README


%changelog
* Wed Jul 26 2017 Vincent Batts <vbatts@fedoraproject.org> - 0.1-0.git426cfd8
- initial packaging
