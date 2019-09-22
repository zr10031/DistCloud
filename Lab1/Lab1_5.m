%function [d,t] = Lab1_5(np, nd)
%if (nargin < 1), np = 1e6; nd = 10; end
np = 1e6; nd = 2;
hp = gcp('nocreate');
if (isempty(hp)), hp = parpool(8); end

aA = randn(np, nd); aB = randn(np, nd);
dA = distributed(aA); dB = distributed(aB);
d = zeros(np, 1);
tic;
dc = sqrt(sum((dA-dB).^2,2));
d = gather(dc);
t = toc;