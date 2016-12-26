// Copyright 2016 Nevio Vesic
// Please check out LICENSE file for more information about limitations
// MIT License

package main

import (
	disposable "github.com/0x19/disposable/protos"
	log "github.com/Sirupsen/logrus"
	uuid "github.com/satori/go.uuid"
	"golang.org/x/net/context"
)

// Verify -
func (s *Service) Verify(c context.Context, req *disposable.DisposableRequest) (*disposable.DisposableResponse, error) {
	log.Infof("[verify] Starting email verification process (req: %v)", req)

	if err := ValidateEmail(req.Email); err != nil {
		log.Errorf("[verify] Could not validate email address due to (err: %s)", err)
	}

	if ok := s.DisposableEmails.IsOK(req.Email); !ok {
		log.Errorf("[verify] Seems like provided (email: %s) is blacklisted!", req.Email)
		return &disposable.DisposableResponse{
			Status:    false,
			RequestId: uuid.NewV4().String(),
			Error:     disposable.NewError(ErrorDomainNotPermitted, TypeDomainNotPermitted, nil),
		}, nil
	}

	return &disposable.DisposableResponse{
		Status:    true,
		RequestId: uuid.NewV4().String(),
	}, nil
}
