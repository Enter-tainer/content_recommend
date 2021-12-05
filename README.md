# 相关文章推荐

1. 首先用 strip_md.js 生成 strip 后的 md 文件
2. 然后使用 generate_vector.py 生成文章向量
3. 这样就可以使用 get_nearest.py 进行相似文章搜索了，可以使用 get_file_list.py 获取文章的列表和对应的编号

## 示例

```
res for ../OI-Wiki/docs/lang/csl/iterator.md.stripped.npy :
../OI-Wiki/docs/lang/csl/sequence-container.md
../OI-Wiki/docs/lang/csl/container.md
../OI-Wiki/docs/lang/csl/associative-container.md
../OI-Wiki/docs/ds/stack.md

res for ../OI-Wiki/docs/ds/heap.md.stripped.npy :
../OI-Wiki/docs/ds/binary-heap.md
../OI-Wiki/docs/lang/pb-ds/pq.md
../OI-Wiki/docs/topic/rmq.md
../OI-Wiki/docs/ds/sqrt-tree.md

res for ../OI-Wiki/docs/math/poly/fft.md.stripped.npy :
../OI-Wiki/docs/math/poly/ntt.md
../OI-Wiki/docs/math/quick-pow.md
../OI-Wiki/docs/math/poly/lagrange.md
../OI-Wiki/docs/math/number-theory/inverse.md

res for ../OI-Wiki/docs/math/combinatorics/catalan.md.stripped.npy :
../OI-Wiki/docs/graph/lgv.md
../OI-Wiki/docs/graph/mod-shortest-path.md
../OI-Wiki/docs/geometry/nearest-points.md
../OI-Wiki/docs/ds/fenwick.md

res for ../OI-Wiki/docs/math/number-theory/gcd.md.stripped.npy :
../OI-Wiki/docs/math/number-theory/bezouts.md
../OI-Wiki/docs/math/quick-pow.md
../OI-Wiki/docs/math/number-theory/basic.md
../OI-Wiki/docs/math/poly/shift.md

res for ../OI-Wiki/docs/math/number-theory/min-25.md.stripped.npy :
../OI-Wiki/docs/math/number-theory/powerful-number.md
../OI-Wiki/docs/math/number-theory/zhou.md
../OI-Wiki/docs/math/number-theory/du.md
../OI-Wiki/docs/math/combinatorics/inclusion-exclusion-principle.md

res for ../OI-Wiki/docs/string/bm.md.stripped.npy :
../OI-Wiki/docs/string/kmp.md
../OI-Wiki/docs/string/z-func.md
../OI-Wiki/docs/string/manacher.md
../OI-Wiki/docs/dp/opt/state.md

res for ../OI-Wiki/docs/tools/editor/vscode.md.stripped.npy :
../OI-Wiki/docs/tools/editor/devcpp.md
../OI-Wiki/docs/lang/helloworld.md
../OI-Wiki/docs/tools/editor/kate.md
../OI-Wiki/docs/tools/editor/geany.md

res for ../OI-Wiki/docs/basic/bucket-sort.md.stripped.npy :
../OI-Wiki/docs/basic/heap-sort.md
../OI-Wiki/docs/basic/shell-sort.md
../OI-Wiki/docs/basic/sort-intro.md
../OI-Wiki/docs/basic/quick-sort.md
```
