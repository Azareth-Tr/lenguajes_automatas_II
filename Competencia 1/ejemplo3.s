	.file	"ejemplo3.c"
	.text
	.section .rdata,"dr"
.LC1:
	.ascii "Aprobado\0"
.LC3:
	.ascii "Reprobado\0"
	.text
	.globl	evaluacionNota
	.def	evaluacionNota;	.scl	2;	.type	32;	.endef
	.seh_proc	evaluacionNota
evaluacionNota:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	movsd	%xmm0, 16(%rbp)
	movsd	16(%rbp), %xmm0
	comisd	.LC0(%rip), %xmm0
	jbe	.L9
	leaq	.LC1(%rip), %rax
	movq	%rax, %rcx
	call	printf
	jmp	.L4
.L9:
	movsd	16(%rbp), %xmm0
	pxor	%xmm1, %xmm1
	comisd	%xmm1, %xmm0
	jbe	.L4
	leaq	.LC3(%rip), %rax
	movq	%rax, %rcx
	call	printf
.L4:
	movl	$0, %eax
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
	.align 8
.LC0:
	.long	0
	.long	1075576832
	.ident	"GCC: (Rev5, Built by MSYS2 project) 16.1.0"
	.def	printf;	.scl	2;	.type	32;	.endef
